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
## Retail AI Location Strategy with Google ADK : Autonomous Site Selection & Market Analysis 
```bash
uvx --from agent-starter-pack agent-starter-pack create retail-ai-location-strategy --adk
cd retail-ai-location-strategy
source .venv/bin/activate
uv sync
adk web . --port 8501 --reload_agents
```
