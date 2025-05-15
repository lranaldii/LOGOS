import argparse
import logging

from prompt_framework.orchestrator import PipelineBuilder, Orchestrator
from prompt_framework.client import OpenAIClient

def main():
    parser = argparse.ArgumentParser(
        prog="logos-cli",
        description="LOGOS: Modular Prompt Framework CLI"
    )
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to the pipeline configuration file"
    )
    parser.add_argument(
        "--question",
        required=True,
        help="The question to process through the LOGOS pipeline"
    )
    parser.add_argument(
        "--api-key",
        required=True,
        help="API key for the OpenAI service"
    )
    parser.add_argument(
        "--model",
        default="gpt-4",
        help="Name of the LLM model to use"
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Logging level (DEBUG, INFO, WARNING, ERROR)"
    )
    args = parser.parse_args()

    # build and run the pipeline
    builder = PipelineBuilder(args.config)
    modules = builder.load_modules()
    client = OpenAIClient(api_key=args.api_key, model=args.model)
    orchestrator = Orchestrator(
        modules=modules,
        llm_client=client,
        log_level=getattr(logging, args.log_level.upper())
    )

    results = orchestrator.execute(args.question)
    for name, text in results.items():
        print(f"\n=== [{name}] ===\n{text}\n")

if __name__ == "__main__":
    main()
