---
name: agentic-tool-integrations-and-mcp
description: >-
  Design and integrate tools using the Model Context Protocol (MCP), REST APIs, and webhook event architectures. Use when connecting agents to external databases, custom execution servers, or third-party enterprise tools.
---

# Agentic Tool Integrations, APIs & Model Context Protocol (MCP)

## Overview
Synthesized from **Chapter 2 of The 5 Levels of AI Mastery**, this skill covers tool definitions, parameter schemas, Model Context Protocol (MCP) servers, and robust error-handling protocols for agent-tool interactions.

---

## 1. Model Context Protocol (MCP) Configuration
Antigravity and Gemini agents connect to external tools via `mcp_config.json`:

```json
{
  "mcpServers": {
    "custom_tools": {
      "command": "python",
      "args": ["-m", "my_mcp_server"],
      "env": {
        "API_TOKEN": "secret_key"
      }
    }
  }
}
```

---

## 2. Rigid Tool Schema Design Principles
1. **Strong Typing & Explicit Descriptions**: Every parameter must have an explicit JSON Schema `type`, `description`, and `required` flag.
2. **Deterministic Outputs**: Tools must return structured JSON or plain text with explicit status indicators (`STATUS: SUCCESS` / `STATUS: ERROR`).
3. **Error Transparency**: Never swallow exceptions. Return exact error codes, system messages, and actionable troubleshooting steps so the agent can self-correct.
