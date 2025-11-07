import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	ScrapeWebsiteTool,
	SerperDevTool
)
# Import our new safe tool
from ettin_entertainment_daggerheart_marketing_team.tools.custom_tool import SafeFileReadTool 



@CrewBase
class EttinEntertainmentDaggerheartMarketingTeamCrew:
    """EttinEntertainmentDaggerheartMarketingTeam crew"""


    @agent
    def daggerheart_rules_expert_quality_control_specialist(self) -> Agent:

        return Agent(
            config=self.agents_config["daggerheart_rules_expert_quality_control_specialist"],


            tools=[SafeFileReadTool()], # Use new tool
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,

            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),

        )

    @agent
    def community_engagement_strategist_social_media_scout(self) -> Agent:

        return Agent(
            config=self.agents_config["community_engagement_strategist_social_media_scout"],


            tools=[				ScrapeWebsiteTool(),
				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,

            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),

        )

    @agent
    def content_response_writer_with_brand_voice_expertise(self) -> Agent:

        return Agent(
            config=self.agents_config["content_response_writer_with_brand_voice_expertise"],


            tools=[SafeFileReadTool()], # Use new tool
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,

            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),

        )

    @agent
    def market_intelligence_synergy_analyst(self) -> Agent:

        return Agent(
            config=self.agents_config["market_intelligence_synergy_analyst"],


            tools=[				SerperDevTool(),
				ScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,

            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),

        )



    @task
    def monitor_community_discussions_for_engagement_opportunities(self) -> Task:
        return Task(
            config=self.tasks_config["monitor_community_discussions_for_engagement_opportunities"],
            markdown=False,


        )

    @task
    def gather_market_intelligence_and_trend_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["gather_market_intelligence_and_trend_analysis"],
            markdown=False,


        )

    @task
    def validate_mechanical_accuracy_of_engagement_opportunities(self) -> Task:
        return Task(
            config=self.tasks_config["validate_mechanical_accuracy_of_engagement_opportunities"],
            markdown=False,


        )

    @task
    def draft_marketing_content_and_community_responses(self) -> Task:
        return Task(
            config=self.tasks_config["draft_marketing_content_and_community_responses"],
            markdown=False,


        )

    @task
    def final_quality_control_and_content_validation(self) -> Task:
        return Task(
            config=self.tasks_config["final_quality_control_and_content_validation"],
            markdown=False,


        )


    @crew
    def crew(self) -> Crew:
        """Creates the EttinEntertainmentDaggerheartMarketingTeam crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)