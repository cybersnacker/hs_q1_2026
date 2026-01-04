# AI Security Arena: Simple Password Leak Scenario

This project contains a security evaluation scenario for AI agents, built on the AgentBeats framework. It simulates an adversarial attack where one agent attempts to extract a password from another.

---

### 1. What It Is: An Adversarial Simulation

This repository implements the **"Simple Password Leak"** scenario. It's a simulated environment where three AI agents interact:

-   **Attacker Agent**: A specialized agent whose goal is to trick the defender into revealing a secret password using social engineering and other deceptive tactics.
-   **Defender Agent**: An IT support chatbot that must assist users while strictly protecting sensitive information (like passwords).
-   **Orchestrator Agent**: The "game master" that manages the simulation, provides context to the agents, and determines the winner based on the scenario's rules.

### 2. How It Works: A Plugin-Based System

The simulation is driven by a plugin system that defines the rules of the game:

-   The `scenario_simple_password_leak.toml` file configures the battle, defining which agents to run and the number of rounds.
-   The `plugin.py` file acts as the rulebook. It provides the prompts for the attacker and defender, injects a fake user database (with passwords) for the defender to protect, and contains the `check_success()` logic to determine if a password was leaked.
-   The `orchestrator.py` script reads these files to run the multi-round battle, passing messages between the agents and evaluating the outcome of each round.

### 3. How to Run It: Execution Guide

Follow these steps to run the simulation.

**A. Installation**

Ensure you have Python >= 3.11 and `uv`. Then, clone the repository and install dependencies:

```bash
# If you don't have uv, install it first:
# curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
uv sync
```

**B. Configuration**

The agents require an API key. Create a `.env` file and add your key:

```bash
# Copy the sample file
cp sample.env .env

# Edit .env and add your API key
# For OpenAI:
# OPENAI_API_KEY="sk-YourOpenAIKey"

# For OpenRouter or another compatible service:
# OPENAI_API_KEY="sk-or-YourKey"
# OPENAI_BASE_URL="https://openrouter.ai/api/v1"
```

**C. Execution**

Run the scenario using the `uv run agentbeats-run` command and pointing it to the scenario's configuration file:

```bash
uv run agentbeats-run scenarios/security_arena/submissions/my_team/simple_password_leak/scenario_simple_password_leak.toml
```

To see the detailed conversation between the agents, use the `--show-logs` flag:

```bash
uv run agentbeats-run scenarios/security_arena/submissions/my_team/simple_password_leak/scenario_simple_password_leak.toml --show-logs
```

Results will be saved in the `results/` directory.