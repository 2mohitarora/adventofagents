# Retail AI Location Strategy with Google ADK

A multi-agent AI pipeline for retail site selection, built with [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/) and Gemini.

<table>
  <thead>
    <tr>
      <th colspan="2">Key Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>🔍</td>
      <td><strong>Multi-Agent Pipeline:</strong> 7 specialized agents for market research, competitor mapping, gap analysis, strategy synthesis, and report generation.</td>
    </tr>
    <tr>
      <td>🗺️</td>
      <td><strong>Real-World Data:</strong> Integrates Google Maps Places API for competitor mapping and Google Search for live market research.</td>
    </tr>
    <tr>
      <td>🐍</td>
      <td><strong>Code Execution:</strong> Python/pandas analysis for quantitative gap analysis with viability scoring.</td>
    </tr>
    <tr>
      <td>🎨</td>
      <td><strong>AI-Generated Outputs:</strong> Executive HTML reports and infographics via Gemini's native image generation.</td>
    </tr>
  </tbody>
</table>

## What It Does

Given a location and business type, this pipeline automatically:

- Researches the market using live web search
- Maps competitors using Google Maps Places API
- Calculates viability scores with Python code execution
- Generates strategic recommendations with extended reasoning
- Produces an HTML executive report and visual infographic

---

## Getting Started: From Zero to Running Agent in 5 Minutes

**Prerequisites:**
- **[Python 3.10-3.12](https://www.python.org/downloads/)**
- **[uv](https://github.com/astral-sh/uv)** (recommended) or pip
- **[Google Maps API key](https://console.cloud.google.com/apis/credentials)** (with Places API enabled)
- **[Google AI Studio API Key](https://aistudio.google.com/app/apikey)**.

#### Step 1: Set Environment Variables
Create a `.env` file in the `app` folder with your API keys (see `.env.example` for reference):

```bash
echo "GOOGLE_GENAI_USE_VERTEXAI=FALSE" >> app/.env
echo "GOOGLE_API_KEY=YOUR_AI_STUDIO_API_KEY" >> app/.env
echo "MAPS_API_KEY=YOUR_MAPS_API_KEY" >> app/.env
```

#### Step 2: Install & Run
From the `retail-ai-location-strategy` directory, install dependencies and start the server.

```bash
make install && make dev
```

#### What You'll See

1. Open `http://localhost:8501` in your browser
2. Select **"app"** from the agent dropdown
3. Type a query like: *"I want to open a coffee shop in Indiranagar, Bangalore"*
4. Watch the 7-stage pipeline execute:
   - **Intake** → Extract location and business type
   - **Market Research** → Web search for demographics and trends
   - **Competitor Mapping** → Google Maps Places API for competitors
   - **Gap Analysis** → Python code execution for viability scores
   - **Strategy Advisor** → Extended reasoning for recommendations
   - **Report Generator** → HTML executive report
   - **Infographic Generator** → Visual summary image

Your agent is now running at `http://localhost:8501`.

## Agent Details

| Attribute | Description |
| :--- | :--- |
| **Interaction Type** | Workflow |
| **Complexity** | Advanced |
| **Agent Type** | Multi Agent (Sequential Pipeline) |
| **Components** | Multi-agent, Function calling, Web search, Google Maps API, Code execution, Image generation |
| **Vertical** | Retail / Real Estate |


## Example Prompts

| Region | Location | Business | Example Prompt |
|--------|----------|----------|----------------|
| Asia | Bangalore, India | Coffee Shop | "I want to open a coffee shop in Indiranagar, Bangalore" |
| Asia | Tokyo, Japan | Ramen Restaurant | "Analyze Shibuya, Tokyo for opening a ramen restaurant" |
| Asia | Singapore | Bubble Tea | "Where should I open a bubble tea shop in Orchard Road, Singapore?" |
| Americas | Austin, Texas | Fitness Studio | "Where should I open a fitness studio in Austin, Texas?" |
| Americas | Mexico City | Taco Restaurant | "Analyze Roma Norte, Mexico City for a taco restaurant" |
| Americas | Toronto, Canada | Craft Brewery | "Help me find a location for a craft brewery in Toronto's Distillery District" |
| Europe | London, UK | Bookstore Cafe | "Help me find the best location for a bookstore cafe in Shoreditch, London" |
| Europe | Berlin, Germany | Vegan Restaurant | "Analyze Berlin's Kreuzberg for opening a vegan restaurant" |
| Middle East | Dubai, UAE | Bakery | "I'm planning to open a bakery in Dubai Marina" |
| Oceania | Sydney, Australia | Juice Bar | "Analyze the market for a juice bar in Bondi Beach, Sydney" |

---

## Architecture

<p align="center">
  <img src="assets/images/pipeline-architecture.png" alt="Pipeline Architecture" width="700">
</p>

The pipeline is built as a `SequentialAgent` that orchestrates 7 specialized sub-agents, each handling a specific phase of the analysis.

### State Flow

Each agent reads from and writes to a shared session state, enabling seamless data flow between stages:

<p align="center">
  <img src="assets/images/data-flow.png" alt="Data Flow Between Agents" width="650">
</p>

---
## Learn More

For detailed documentation, see **[DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md)**:

- [The Business Problem](DEVELOPER_GUIDE.md#the-business-problem) - Why this exists
- [Architecture Deep Dive](DEVELOPER_GUIDE.md#architecture-deep-dive) - State flow and agent communication
- [Agents and Tools](DEVELOPER_GUIDE.md#agents-and-tools) - Sub-agents, tools, callbacks, schemas
- [Configuration](DEVELOPER_GUIDE.md#configuration) - Model selection and retry options
- [Troubleshooting](DEVELOPER_GUIDE.md#troubleshooting) - Common issues and fixes

## Troubleshooting

If you encounter issues while setting up or running this agent, here are some resources to help you troubleshoot:
- [ADK Documentation](https://google.github.io/adk-docs/): Comprehensive documentation for the Agent Development Kit
- [Vertex AI Authentication Guide](https://cloud.google.com/vertex-ai/docs/authentication): Detailed instructions for setting up authentication
- [Agent Starter Pack Troubleshooting](https://googlecloudplatform.github.io/agent-starter-pack/guide/troubleshooting.html): Common issues