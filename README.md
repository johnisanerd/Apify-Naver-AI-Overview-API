# 🟢 Naver AI Overview API: track Korean AI answers as clean JSON

> The most efficient, reliable, and developer-friendly way to use the Naver AI Overview API.

**Actor page:** [apify.com/johnvc/naver-ai-overview-api](https://apify.com/johnvc/naver-ai-overview-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/naver-ai-overview-api/input-schema](https://apify.com/johnvc/naver-ai-overview-api/input-schema?fpr=9n7kx3)

Track Naver's AI Overview answers for any query and get the AI-generated overview, its cited sources, and related media as structured JSON. Naver is South Korea's largest search engine, and its AI answers increasingly shape what Korean users see first. Use this API to monitor whether your brand, product, or topic appears in those answers, and which sources Naver cites. This is a brand-monitoring and answer-engine-optimization (AEO) tool.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Naver-AI-Overview-API.git
   cd Apify-Naver-AI-Overview-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python naver-ai-overview-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python naver-ai-overview-api-example.py
```

## Why Use This Naver AI Overview API?

Monitor your AEO footprint in Korea. See whether Naver's AI answer mentions you, and which sources it cites, across a list of brand and category queries.

Clean, structured output. Each query returns one row: the answer as markdown, structured text blocks, cited references, and related media. Load it straight into a dataframe or dashboard.

Built for batch monitoring. Pass a list of queries and check a whole topic set in one run, then schedule it to track changes over time.

MCP-ready. AI agents can call it as a tool through the hosted Apify MCP server, so an assistant can audit your Naver AI visibility on demand.

## Features

### Core Capabilities
- Resolve the Naver AI Overview for one query or many
- Get the full answer as markdown plus structured text blocks
- See the cited references (title, link, source) behind each answer
- Get related media (videos, images) shown with the answer

### Data Quality
- One clean row per query, with a clear `ai_overview_present` flag
- Reference indexes link text blocks to their sources
- Stable JSON shape, easy to diff run-over-run for monitoring

## Usage Examples

### Basic Example
```json
{
  "query": "당뇨병 증상"
}
```

### Advanced Example
```json
{
  "queries": ["당뇨병 증상", "전기차 보조금", "비타민 D 효능"]
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | `str` | one of query/queries | - | A single query, in Korean or any language, e.g. `당뇨병 증상`. |
| `queries` | `list[str]` | one of query/queries | - | A batch of queries. Merged with `query` and de-duplicated. |

## Output Format

Each item in the dataset is one query's AI Overview:

```json
{
  "result_type": "ai_overview",
  "query": "당뇨병 증상",
  "ai_overview_present": true,
  "markdown": "당뇨병의 주요 증상은 ...",
  "text_blocks": [
    { "type": "paragraph", "snippet": "당뇨병의 주요 증상은 ...", "reference_indexes": [0, 1] }
  ],
  "references": [
    { "index": 0, "title": "당뇨병 - 질병관리청", "link": "https://example.go.kr/...", "source": "질병관리청" }
  ],
  "media": [
    { "title": "당뇨병 증상 설명", "platform": "video", "link": "https://example.com/...", "thumbnail": "https://..." }
  ]
}
```

---

<!-- The five install sections below are the canonical MCP install copy. -->

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Naver AI Overview API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/naver-ai-overview-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Naver AI Overview API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/naver-ai-overview-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/naver-ai-overview-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Naver AI Overview API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/naver-ai-overview-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/naver-ai-overview-api`, using OAuth when prompted.
5. Ask Claude to run the Naver AI Overview API.

Open Claude on the web: https://claude.ai

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/naver-ai-overview-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/naver-ai-overview-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Naver AI Overview API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/naver-ai-overview-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Naver AI Overview API to monitor your brand's visibility in Korean AI search.*

Last Updated: 2026.06.01
