### Setup Environment

```bash
uv init
uv run main.py
uv add google-adk
uv add google-genai
uv add agent-starter-pack
```
## Day2
```bash
uvx --from google-adk adk create --type=config day2
uvx --from google-adk adk web
```
## Day3
```bash
source .venv/bin/activate
adk create day3
adk web
```
## Day6
```bash
source .venv/bin/activate
agent-starter-pack create day6 --adk
adk web
```
