#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODE_DIR="$ROOT_DIR/code/python"

usage() {
  cat <<'EOF'
Usage:
  ./run_questions.sh                # Run all questions in code/python/*.py
  ./run_questions.sh all            # Run all questions in code/python/*.py
  ./run_questions.sh 1 2 17         # Run only selected questions
  ./run_questions.sh 1,2,17         # Comma-separated form also works

Notes:
  - Question numbers map to files like code/python/<number>.py
  - Scripts are executed with: uv run python <file>
EOF
}

run_question() {
  local q="$1"
  local file="$CODE_DIR/${q}.py"

  if [[ ! -f "$file" ]]; then
    echo "[warn] Question ${q} not found at $file" >&2
    return 1
  fi

  echo
  echo "===== Question ${q} ====="
  print_question "$file"
  echo
  echo "----- Answer -----"
  uv run python "$file"
}

print_question() {
  local file="$1"

  echo "----- Prompt -----"
  awk '
    BEGIN {
      in_markdown = 0
      found_block = 0
      previous_blank = 0
    }

    /^# --- Cell [0-9]+ \(markdown\) ---$/ {
      if (!found_block) {
        in_markdown = 1
        found_block = 1
        next
      }
      if (in_markdown) {
        exit
      }
    }

    /^# --- Cell [0-9]+ \(/ {
      if (in_markdown) {
        exit
      }
    }

    {
      if (!in_markdown) {
        next
      }

      line = $0
      sub(/^# ?/, "", line)

      if (line == "") {
        if (!previous_blank) {
          print ""
        }
        previous_blank = 1
        next
      }

      previous_blank = 0
      print line
    }
  ' "$file"
}

collect_all_questions() {
  find "$CODE_DIR" -maxdepth 1 -type f -name '*.py' \
    | sed -E 's|.*/([0-9]+)\.py$|\1|' \
    | awk '/^[0-9]+$/' \
    | sort -n
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

questions=()

if [[ $# -eq 0 || "${1:-}" == "all" ]]; then
  while IFS= read -r q; do
    questions+=("$q")
  done < <(collect_all_questions)
else
  # Support both space-separated and comma-separated input.
  for arg in "$@"; do
    IFS=',' read -r -a parts <<< "$arg"
    for part in "${parts[@]}"; do
      q="${part%.py}"
      q="${q##*/}"
      if [[ "$q" =~ ^[0-9]+$ ]]; then
        questions+=("$q")
      else
        echo "[warn] Skipping invalid question identifier: $part" >&2
      fi
    done
  done
fi

if [[ ${#questions[@]} -eq 0 ]]; then
  echo "[error] No valid questions to run."
  usage
  exit 1
fi

fail_count=0

for q in "${questions[@]}"; do
  if ! run_question "$q"; then
    ((fail_count+=1))
  fi
done

if [[ $fail_count -gt 0 ]]; then
  echo
  echo "Completed with ${fail_count} missing/failed question(s)." >&2
  exit 1
fi

echo
echo "Completed successfully."
