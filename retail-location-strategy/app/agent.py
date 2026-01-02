from google.adk.agents import SequentialAgent
from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool


from .sub_agents.intake_agent.agent import intake_agent
from .sub_agents.market_research.agent import market_research_agent
from .sub_agents.competitor_mapping.agent import competitor_mapping_agent
from .sub_agents.gap_analysis.agent import gap_analysis_agent
from .sub_agents.strategy_advisor.agent import strategy_advisor_agent
from .sub_agents.infographic_generator.agent import infographic_generator_agent
from .sub_agents.report_generator.agent import report_generator_agent

from .config import FAST_MODEL, APP_NAME

# location_strategy_pipeline
location_strategy_pipeline = SequentialAgent(
    name="LocationStrategyPipeline",
    description="""Comprehensive retail location strategy analysis pipeline.

This agent analyzes a target location for a specific business type and produces:
1. Market research findings from live web data
2. Competitor mapping from Google Maps Places API
3. Quantitative gap analysis with zone rankings
4. Strategic recommendations with structured JSON output
5. Professional HTML executive report
6. Visual infographic summary

To use, get the following details:
- target_location: {target_location}
- business_type: {business_type}

The analysis runs automatically through all stages and produces artifacts
including JSON report, HTML report, and infographic image.
""",
    sub_agents=[
        market_research_agent,      # Part 1: Market research with search
        competitor_mapping_agent,   # Part 2A: Competitor mapping with Maps
        gap_analysis_agent,         # Part 2B: Gap analysis with code exec
        strategy_advisor_agent,     # Part 3: Strategy synthesis
        report_generator_agent,     # Part 4: HTML report generation
        infographic_generator_agent,  # Part 5: Infographic generation
    ],
)

# Root agent orchestrating the complete location strategy pipeline
root_agent = Agent(
    model=FAST_MODEL,
    name=APP_NAME,
    description='A strategic partner for retail businesses, guiding them to optimal physical locations that foster growth and profitability.',
    instruction="""Your primary role is to orchestrate the retail location analysis.
1. Start by greeting the user.
2. Check if the `TARGET_LOCATION` (Geographic area to analyze (e.g., "Manhattan, New York")) and `BUSINESS_TYPE` (Type of business (e.g., "coffee shop", "bakery", "gym")) have been provided.
3. If they are missing, **ask the user clarifying questions to get the required information.**
4. Once you have the necessary details, call the `IntakeAgent` tool to process them.
5. After the `IntakeAgent` is successful, delegate the full analysis to the `LocationStrategyPipeline`.
Your main function is to manage this workflow conversationally.""",
    sub_agents=[location_strategy_pipeline],
    tools = [AgentTool(intake_agent)], # Part 0: Parse user request
)