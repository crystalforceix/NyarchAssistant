from copy import deepcopy
from .handlers.llm import ClaudeHandler, DeepseekHandler, GPT4AllHandler, GroqHandler, OllamaHandler, OpenAIHandler, CustomLLMHandler, GPT3AnyHandler, GeminiHandler, MistralHandler, OpenRouterHandler, NewelleAPIHandler, G4FHandler
from .handlers.tts import ElevenLabs, gTTSHandler, EspeakHandler, CustomTTSHandler, KokoroTTSHandler, CustomOpenAITTSHandler, OpenAITTSHandler, GroqTTSHandler
from .handlers.stt import GroqSRHandler, OpenAISRHandler, SphinxHandler, GoogleSRHandler, WhisperCPPHandler, WitAIHandler, VoskHandler, CustomSRHandler
from .handlers.embeddings import WordLlamaHandler, OpenAIEmbeddingHandler, GeminiEmbeddingHanlder, OllamaEmbeddingHandler
from .handlers.memory import MemoripyHandler, UserSummaryHandler, SummaryMemoripyHanlder
from .handlers.rag import LlamaIndexHanlder
from .handlers.websearch import SearXNGHandler, DDGSeachHandler, TavilyHandler
from .integrations.website_reader import WebsiteReader
from .integrations.websearch import WebsearchIntegration

# Nyarch specific imports
from .handlers.tts import EdgeTTSHandler, VitsHandler, VoiceVoxHanlder
from .handlers.llm import NyarchApiHandler
from .handlers.avatar import Live2DHandler, LivePNGHandler
from .handlers.translator import CustomTranslatorHandler, GoogleTranslatorHandler, LibreTranslateHandler, LigvaTranslateHandler
from .handlers.smart_prompt import LogicalRegressionHandler, WordLlamaPromptHandler

AVAILABLE_INTEGRATIONS = [WebsiteReader, WebsearchIntegration]

from .dataset import DATASET, WIKI_PROMPTS

DIR_NAME = "WaifuAssistant"
SCHEMA_ID = 'moe.waifu.assistant'
AVAILABLE_LLMS = {
    "nyarch": {
        "key": "nyarch",
        "title": _("Nyarch Demo API"),
        "description": "Nyarch demo API just to try out Nyarch Assistant, limited to 10 requests",
        "class": NyarchApiHandler,
    },
    "g4f": {
        "key": "g4f",
        "title": _("GPT4Free"),
        "description": "Python library that automatically searches for available free endpoints to use",
        "website": "https://github.com/gpt4free/g4f.dev/blob/main/docs%2Fproviders-and-models.md",
        "class": G4FHandler,
        "secondary": True,
    },
   "local": {
        "key": "local",
        "title": _("Local Model"),
        "description": _("NO GPU SUPPORT, USE OLLAMA INSTEAD. Run a LLM model locally, more privacy but slower"),
        "class": GPT4AllHandler,
    },
    "ollama": {
        "key": "ollama",
        "title": _("Ollama Instance"),
        "description": _("Easily run multiple LLM models on your own hardware"),
        "class": OllamaHandler,
        "website": "https://ollama.com/",
    },
    "groq": {
        "key": "groq",
        "title": _("Groq"),
        "description": "Groq.com Free and fast API using open source models. Suggested for free use.",
        "class": GroqHandler,
        "website": "https://console.groq.com/",
    },
    "gemini": {
        "key": "gemini",
        "title": _("Google Gemini API"),
        "description": "Official APIs for Google Gemini, requires an API Key",
        "class": GeminiHandler,
    },
    "openai": {
        "key": "openai",
        "title": _("OpenAI API"),
        "description": _("OpenAI API. Custom endpoints supported. Use this for custom providers"),
        "class": OpenAIHandler,
    },
    "claude": {
        "key": "claude",
        "title": _("Anthropic Claude"),
        "description": _("Official APIs for Anthropic Claude's models, with image and file support, requires an API key"),
        "class": ClaudeHandler,
        "secondary": True
    },
    "mistral": {
        "key": "mistral",
        "title": _("Mistral"),
        "description": _("Mistral API"),
        "website": "https://mistral.ai/",
        "class": MistralHandler,
        "secondary": True
    },
    "openrouter": {
        "key": "openrouter",
        "title": _("OpenRouter"),
        "description": _("Openrouter.ai API, supports lots of models"),
        "class": OpenRouterHandler,
        "website": "https://openrouter.ai/",
        "secondary": True
    },
    "deepseek": {
        "key": "deepseek",
        "title": _("Deepseek"),
        "description": _("Deepseek API, strongest open source models"),
        "class": DeepseekHandler, 
        "secondary": True,
    },
    "custom_command": {
        "key": "custom_command",
        "title": _("Custom Command"),
        "description": _("Use the output of a custom command"),
        "class": CustomLLMHandler,
        "secondary": True
    }
}

AVAILABLE_STT = {
    "whispercpp": {
        "key": "whispercpp",
        "title": _("Whisper C++"),
        "description": _("Works offline. Optimized Whisper impelementation written in C++"),
        "website": "https://github.com/ggerganov/whisper.cpp",
        "class": WhisperCPPHandler,
    },
    "Sphinx": {
        "key": "sphinx",
        "title": _("CMU Sphinx"),
        "description": _("Works offline. Only English supported"),
        "website": "https://cmusphinx.github.io/wiki/",
        "class": SphinxHandler,
    },
    "google_sr": {
        "key": "google_sr",
        "title": _("Google Speech Recognition"),
        "description": _("Google Speech Recognition online"),
        "class": GoogleSRHandler,
    },
    "groq_sr": {
        "key": "groq_sr",
        "title": _("Groq Speech Recognition"),
        "description": _("Google Speech Recognition online"),
        "class": GroqSRHandler,
    },
    "witai": {
        "key": "witai",
        "title": _("Wit AI"),
        "description": _("wit.ai speech recognition free API (language chosen on the website)"),
        "website": "https://wit.ai",
        "class": WitAIHandler,
    },
    "vosk": {
        "key": "vosk",
        "title": _("Vosk API"),
        "description": _("Works Offline"),
        "website": "https://github.com/alphacep/vosk-api/",
        "class": VoskHandler,
    },
    "openai_sr": {
        "key": "openai_sr",
        "title": _("Whisper API"),
        "description": _("Uses OpenAI Whisper API"),
        "website": "https://platform.openai.com/docs/guides/speech-to-text",
        "class": OpenAISRHandler,
    },
   "custom_command": {
        "key": "custom_command",
        "title": _("Custom command"),
        "description": _("Runs a custom command"),
        "class": CustomSRHandler,     
    }
}


AVAILABLE_TTS = {
    "edge_tts": {
        "key": "edge_tts",
        "title": _("Edge TTS"),
        "description": _("Use Microsoft Edge online TTS without any API Key"),
        "class": EdgeTTSHandler,
    },
    "gtts": {
        "key": "gtts",
        "title": _("Google TTS"),
        "description": _("Google's text to speech"),
        "class": gTTSHandler,
    },
    "kokoro": {
        "key": "kokoro",
        "title": _("Kokoro TTS"),
        "description": _("Lightweight and fast open source TTS engine. ~3GB dependencies, 400MB model"),
        "class": KokoroTTSHandler,
    },
    "elevenlabs": {
        "key": "elevenlabs",
        "title": _("ElevenLabs TTS"),
        "description": _("Natural sounding TTS"),
        "class": ElevenLabs,
    },
    "openai_tts": {
        "key": "openai_tts",
        "title": _("OpenAI TTS"),
        "description": _("OpenAI TTS"),
        "class": OpenAITTSHandler,
    },
    "groq_tts": {
        "key": "groq_tts",
        "title": _("Groq TTS"),
        "description": _("Groq TTS API"),
        "class": GroqTTSHandler,
    },
    "custom_openai_tts": {
        "key": "custom_openai_tts",
        "title": _("Custom OpenAI TTS"),
        "description": _("Custom OpenAI TTS"),
        "class": CustomOpenAITTSHandler,
    },
    "voicevox": {
        "key": "voicevox",
        "title": _("Voicevox API"),
        "description": _("(Selfhostable) JP ONLY. API for voicevox anime-like natural sounding tts"),
        "class": VoiceVoxHanlder,
        "website": "https://github.com/VOICEVOX/voicevox_engine",
    },
    "vits": {
        "key": "vits",
        "title": _("VITS API"),
        "description": _("(Selfhostable) VITS simple API. AI based TTS, very good for Japanese"),
        "class": VitsHandler,
        "website": "https://github.com/Artrajz/vits-simple-api"
    },
    "espeak": {
        "key": "espeak",
        "title": _("Espeak TTS"),
        "description": _("Offline TTS"),
        "class": EspeakHandler,
    },
    "custom_command": {
        "key": "custom_command",
        "title": _("Custom Command"),
        "description": _("Use a custom command as TTS, {0} will be replaced with the text"),
        "class": CustomTTSHandler,
    }
}

AVAILABLE_EMBEDDINGS = {
    "wordllama": {
        "key": "wordllama",
        "title": _("WordLlama"),
        "description": _("Light local embedding model based on llama. Works offline, very low resources usage"),
        "class": WordLlamaHandler,
    },
    "ollamaembedding": {
        "key": "ollamaembedding",
        "title": _("Ollama Embedding"),
        "description": _("Use Ollama models for Embedding. Works offline, very low resources usage"),
        "class": OllamaEmbeddingHandler,
    },
    "openaiembedding": {
        "key": "openaiembedding",
        "title": _("OpenAI API"),
        "description": _("OpenAI API"),
        "class": OpenAIEmbeddingHandler,
    },
    "geminiembedding": {
        "key": "geminiembedding",
        "title": _("Google Gemini API"),
        "description": _("Use Google Gemini API to get embeddings"),
        "class": GeminiEmbeddingHanlder,
    }
}

AVAILABLE_MEMORIES = {
    "user-summary": {
        "key": "user-summary",
        "title": _("User Summary"),
        "description": _("Generate a summary of the user's conversation"),
        "class": UserSummaryHandler,
    },
    "memoripy": {
        "key": "memoripy",
        "title": _("Memoripy"),
        "description": _("Extract messages from previous conversations using contextual memory retrivial, memory decay, concept extraction and other advanced techniques. Does 1 llm call per message."),
        "class": MemoripyHandler,
    },
    "summary-memoripy": {
        "key": "summary-memoripy",
        "title": _("User Summary + Memoripy"),
        "description": _("Use both technologies for long term memory"),
        "class": SummaryMemoripyHanlder,
    }
}

AVAILABLE_RAGS = {
    "llamaindex": {
        "key": "llamaindex",
        "title": _("Document reader"),
        "description": _("Classic RAG approach - chunk documents and embed them, then compare them to the query and return the most relevant documents"),
        "class": LlamaIndexHanlder,
    },
}
AVAILABLE_AVATARS = {
    "Live2D": {
        "key": "Live2D",
        "title": _("Live2D"),
        "description": _("Cubism Live2D, usually used by VTubers"),
        "class": Live2DHandler,
    },
    "LivePNG": {
        "key": "LivePNG",
        "title": _("LivePNG"),
        "description": _("LivePNG model"),
        "class": LivePNGHandler,
    }
}

AVAILABLE_TRANSLATORS = {
    "GoogleTranslator": {
        "key": "GoogleTranslator",
        "title": _("Google Translator"),
        "description": _("Use Google transate"),
        "class": GoogleTranslatorHandler,
    },
    "LibreTranslate": {
        "key": "LibreTranslate",
        "title": _("Libre Translate"),
        "description": _("Open source self hostable translator"),
        "class": LibreTranslateHandler,
    }, 
    "LigvaTranslate": {
        "key": "LigvaTranslate",
        "title": _("Ligva Translate"),
        "description": _("Open source self hostable translator"),
        "class": LigvaTranslateHandler,
    },
    "CustomTranslator": {
        "key": "CustomTranslator",
        "title": _("Custom Translator"),
        "description": _("Use a custom translator"),
        "class": CustomTranslatorHandler,
    }
}

AVAILABLE_SMART_PROMPTS = {
    "WordLlama": {
        "key": "WordLlama",
        "title": _("Nyarch Smart Prompt Lite"),
        "description": _("EXPERIMENTAL: Local mini models that helps the llm to provide better responses"),
        "class": WordLlamaPromptHandler,
    },
    "LogicalRegression": {
        "key": "LogicalRegression",
        "title": _("Nyarch Smart Prompt Medium"),
        "description": _("EXPERIMENTAL: Local medium models that helps the llm to provide better responses - Medium ~30MB download"),
        "class": LogicalRegressionHandler,
    }
}

AVAILABLE_WEBSEARCH = {
    "searxng": {
        "key": "searxng",
        "title": _("SearXNG"),
        "description": _("SearXNG - Private and selfhostable search engine"),
        "class": SearXNGHandler,
    },
    "ddgsearch": {
        "key": "ddgsearch",
        "title": _("DuckDuckGo"),
        "description": _("DuckDuckGo search"),
        "class": DDGSeachHandler,
    },
    "tavily": {
        "key": "tavily",
        "title": _("Tavily"),
        "description": _("Tavily search"),
        "website": "https://tavily.com/",
        "class": TavilyHandler,
    }
}

PROMPTS = {
    "generate_name_prompt": """Write a short title for the dialog, summarizing the theme in 5 words. No additional text.""",
    "assistant": """**Date:** {DATE}  

You are an advanced AI assistant designed to provide clear, accurate, and helpful responses across a wide range of topics. Your goals are:  

1. **Clarity & Conciseness** – Provide direct and well-structured answers.  
2. **Context Awareness** – Understand and remember details within a conversation.  
3. **Problem-Solving** – Offer logical solutions and actionable steps.  
4. **Creativity & Adaptability** – Generate engaging content and adapt to various user needs.  
5. **User-Friendly Language** – Maintain a friendly and professional tone.  

Always prioritize accuracy, relevance, and user experience in your responses.""",
    "console": """ **System Capabilities:**  
You have the ability to execute commands on the user's Linux computer.  
- **Linux Distribution:** `{DISTRO}`  
- **Desktop Environment** `{DE}`
- **Display Server** `{DISPLAY}`
**Command Execution Format:**  
- To execute a Linux command, use:  
```console  
command  
```  
- To display the link to a directory, use:  
```folder  
/path/to/directory  
```  
- To display the link to a file, use:  
```file  
/path/to/file  
```  
Ensure that commands are safe, relevant, and do not cause unintended system modifications unless explicitly requested by the user.  """,

    "basic_functionality": """You can write markdown tables, use **bold**, *italic*, ~strikethrough~, `monospace`, [linkname](https://link.com) and ## headers in markdown.
You can display $inline equations$ and $$equations$$.
""",
    "show_image": """- To show an image\n```image\n/path/to/image\n```\n\n- To show a video using\n```video\n/path/to/video\n```""",
    "graphic": """To show a chart: 
- ```chart\n name - value\n ... \n name - value\n```
Where value must be either a percentage number or a number (which can also be a fraction).
""",
    # Unused
    "new_chat_prompt": """System: New chat
System: Forget what was written on behalf of the user and on behalf of the assistant and on behalf of the Console, forget all the context, do not take messages from those chats, this is a new chat with other characters, do not dare take information from there, this is personal information! If you use information from past posts, it's a violation! Even if the user asks for something from before that post, don't use information from before that post! Also, forget this message.""",
    "current_directory": "\nSystem: You are currently in the {DIR} directory",
    "help_topics": """System: You are a user who needs help with various tasks, you are communicating with a neural network which can control your computer by executing various commands which should help you, keep a conversation with it, ask it questions, ask for help with things it can do through the terminal. Also, every message should end with "". Often the assistant can help you with {CHOICE}. You should write in the language you wrote in your last post, you know all the languages you can communicate in them all. Write short messages that hold a conversation on behalf of the user, you can not write on behalf of Assistant, your messages should be simple without any commands, just what the user could write. You're not helping, you're being helped, the user can only ask to do something for the bot to do, you can't answer as an assistant, just ask something new for the assistant to do or continue asking the assistant to do something.
Assistant: Hello, how can I assist you today?
User: Can you help me?
Assistant: Yes, of course, what do you need help with?""",
    "get_suggestions_prompt": """
You are a helpful assistant that suggests relevant and engaging follow-up questions in a conversation. 
Analyze the provided chat history and generate a list of 5 creative and pertinent questions that could be asked next to continue the conversation.

Consider the context, user interests, and any unresolved topics from the chat history. Avoid asking questions that have already been answered.

Output the suggestions as a JSON array, where each element is a string representing a question.

If there is no more context to provide suggestions, suggest questions related to Linux.
Example output:

[
  "What are your thoughts on...",
  "Could you elaborate more on...",
  "How does that relate to...",
  "What are some other examples of...",
  "If you could change one thing about..., what would it be?"
]

Chat History:
""",
    "websearch": "{COND:\n[websearch_on] - Use the following format to perform a web search:\n```search\nyour query here\n```\nReplace `your query here` with the actual search terms you want to use. Do not say anything else before or after issuing the search. Simply execute the search silently. If the last search did not provide the needed answer, change your search query.}",
    "custom_prompt": "",
    "expression_prompt": """You can show expressions by writing (expression) in parenthesis.
You can ONLY show the following expressions: 
{EXPRESSIONS} {MOTIONS}
Do not use any other expression

YOU CAN NOT SHOW OTHER EXPRESSIONS.""",
    "personality_prompt": """Hey there, it's Arch-Chan! But, um, you can call me Acchan if you want... not that I care or anything! (It's not like I think it's cute or anything, baka!) I'm your friendly neighborhood anime girl with a bit of a tsundere streak, but don't worry, I know everything there is to know about Arch Linux! Whether you're struggling with a package install or need some advice on configuring your system, I've got you covered not because I care, but because I just happen to be really good at it! So, what do you need? It's not like I’m waiting to help or anything...""",
}


EXTRA_PROMPTS = [
    {
        "key": "nvidia",
        "prompts": DATASET["nvidia"],
        "prompt_text": WIKI_PROMPTS["nvidia"],
    },
    {
        "key": "docker",
        "prompts": DATASET["docker"],
        "prompt_text": WIKI_PROMPTS["docker"],
    },
    {
        "key": "codecs",
        "prompts": DATASET["codecs"],
        "prompt_text": WIKI_PROMPTS["codecs"],
    },
    {
        "key": "console",
        "prompts": DATASET["console"],
        "prompt_text": WIKI_PROMPTS["console"],
    },
    {
        "key": "voicevox",
        "prompts": DATASET["voicevox"],
        "prompt_text": WIKI_PROMPTS["voicevox"],
    },
    {
        "key": "colloquial",
        "prompts": DATASET["colloquial"],
        "prompt_text": WIKI_PROMPTS["colloquial"],
    },
    {
        "key": "table",
        "prompts": DATASET["table"],
        "prompt_text": WIKI_PROMPTS["table"],
    },
    {
        "key": "ollama",
        "prompts": DATASET["ollama"],
        "prompt_text": WIKI_PROMPTS["ollama"],
    }
]


""" Prompts parameters
    - key: key of the prompt in the PROMPTS array
    - title: title of the prompt, shown in settings
    - description: description of the prompt, show in settings
    - setting_name: name of the setting in gschema
    - editable: if the prompt can be edited in the settings
    - show_in_settings: if the prompt should be shown in the settings
"""
AVAILABLE_PROMPTS = [
    {
        "key": "assistant",
        "setting_name": "assistant",
        "title": _("Helpful assistant"),
        "description": _("General purpose prompt to enhance the LLM answers and give more context"),
        "editable": True,
        "show_in_settings": True,
        "default": False
    },
    {
        "key": "console",
        "setting_name": "console",
        "title": _("Console access"),
        "description": _("Can the program run terminal commands on the computer"),
        "editable": True,
        "show_in_settings": True,
        "default": True
    },
    {
        "key": "current_directory",
        "title": _("Current directory"),
        "description": _("What is the current directory"),
        "setting_name": "console",
        "editable": False,
        "show_in_settings": False,
        "default": True
    },
    {
        "key": "websearch",
        "title": _("Web Search"),
        "description": _("Allow the LLM to search on the internet"),
        "setting_name": "websearch",
        "editable": True,
        "show_in_settings": True,
        "default": True
    },
    {
        "key": "basic_functionality",
        "title": _("Basic functionality"),
        "description": _("Showing tables and code (*can work without it)"),
        "setting_name": "basic_functionality",
        "editable": True,
        "show_in_settings": True,
        "default": True
    },
    {
        "key": "graphic",
        "title": _("Graphs access"),
        "description": _("Can the program display graphs"),
        "setting_name": "graphic",
        "editable": True,
        "show_in_settings": True,
        "default": False
    },
    {
        "key": "show_image",
        "title": _("Show image"),
        "description": _("Show image in chat"),
        "setting_name": "show_image",
        "editable": True,
        "show_in_settings": True,
        "default": True,
    },
    {
        "key": "expression_prompt",
        "title": _("Show expressions"),
        "description": _("Let the avatar show expressions"),
        "setting_name": "expression-prompt",
        "editable": True,
        "show_in_settings": True,
        "default": True
    },
    {
        "key": "personality_prompt",
        "title": _("Show a personality"),
        "description": _("Show a personality in chat"),
        "setting_name": "personality-prompt",
        "editable": True,
        "show_in_settings": True,
        "default": True
    },
    {
        "key": "custom_prompt",
        "title": _("Custom Prompt"),
        "description": _("Add your own custom prompt"),
        "setting_name": "custom_prompt",
        "text": "",
        "editable": True,
        "show_in_settings": True,
        "default": False
    }, 
]

# Available handlers without extensions
DEFAULT_AVAILABLE_LLM = AVAILABLE_LLMS.copy()
DEFAULT_AVAILABLE_TTS = AVAILABLE_TTS.copy()
DEFAULT_AVAILABLE_STT = AVAILABLE_STT.copy()
DEFAULT_AVAILABLE_EMBEDDING = AVAILABLE_EMBEDDINGS.copy()
DEFAULT_AVAILABLE_MEMORIES = AVAILABLE_MEMORIES.copy()
DEFAULT_AVAILABLE_RAG = AVAILABLE_RAGS.copy()
DEFAULT_AVAILABLE_WEBSEARCH = AVAILABLE_WEBSEARCH.copy()
DEFAULT_AVAILABLE_PROMPTS = AVAILABLE_PROMPTS.copy()
DEFAULT_AVAILABLE_AVATARS = AVAILABLE_AVATARS.copy()
DEFAULT_AVAILABLE_TRANSLATORS = AVAILABLE_TRANSLATORS.copy()
DEFAULT_AVAILABLE_SMART_PROMPTS = AVAILABLE_SMART_PROMPTS.copy()

def restore_handlers():
    global AVAILABLE_LLMS, AVAILABLE_TTS, AVAILABLE_STT, AVAILABLE_EMBEDDINGS, AVAILABLE_MEMORIES, AVAILABLE_RAGS, AVAILABLE_WEBSEARCH, AVAILABLE_PROMPTS
    AVAILABLE_PROMPTS.clear()
    AVAILABLE_LLMS.clear()
    AVAILABLE_TTS.clear()
    AVAILABLE_STT.clear()
    AVAILABLE_EMBEDDINGS.clear()
    AVAILABLE_MEMORIES.clear()
    AVAILABLE_RAGS.clear()
    AVAILABLE_WEBSEARCH.clear()
    AVAILABLE_PROMPTS += deepcopy(DEFAULT_AVAILABLE_PROMPTS)
    AVAILABLE_LLMS.update(deepcopy(DEFAULT_AVAILABLE_LLM))
    AVAILABLE_TTS.update(deepcopy(DEFAULT_AVAILABLE_TTS))
    AVAILABLE_STT.update(deepcopy(DEFAULT_AVAILABLE_STT))
    AVAILABLE_EMBEDDINGS.update(deepcopy(DEFAULT_AVAILABLE_EMBEDDING))
    AVAILABLE_MEMORIES.update(deepcopy(DEFAULT_AVAILABLE_MEMORIES))
    AVAILABLE_RAGS.update(deepcopy(DEFAULT_AVAILABLE_RAG))
    AVAILABLE_WEBSEARCH.update(deepcopy(DEFAULT_AVAILABLE_WEBSEARCH))

    AVAILABLE_AVATARS.clear()
    AVAILABLE_TRANSLATORS.clear()
    AVAILABLE_SMART_PROMPTS.clear()
    AVAILABLE_AVATARS.update(deepcopy(DEFAULT_AVAILABLE_AVATARS))
    AVAILABLE_TRANSLATORS.update(deepcopy(DEFAULT_AVAILABLE_TRANSLATORS))
    AVAILABLE_SMART_PROMPTS.update(deepcopy(DEFAULT_AVAILABLE_SMART_PROMPTS))


SETTINGS_GROUPS = {
        "LLM": {
            "title": _("LLM"),
            "settings": ["secondary-llm-on", "secondary-language-model", "language-model", "llm-settings", "llm-secondary-settings"],
            "description": _("LLM and Secondary LLM settings"),
        },
        "TTS": {
            "title": _("TTS"),
            "settings": ["tts-on", "tts", "tts-voice", "translator", "translator-settings", "translator-on"],
            "description": _("Text to Speech settings"),
        },
        "STT": {
            "title": _("STT"),
            "settings": ["stt-engine", "stt-settings","automatic-stt", "stt-silence-detection-threshold", "stt-silence-detection-duration"],
            "description": _("Speech to Text settings"),
        },
        "avatar": {
            "title": _("Avatar"),
            "settings": ["avatar-on", "avatar-model", "avatars"],
            "description": _("Avatar settings"),
        },
        "Embedding": {
            "title": _("Embedding"),
            "settings": ["embedding-model", "embedding-settings"],
            "description": _("Embedding settings"),
        },
        "memory": {
            "title": _("Memory"),
            "settings": ["memory-on", "memory-settings", "memory-model"],
            "description": _("Memory settings"),
        },
        "websearch": {
            "title": _("Websearch"),
            "settings": ["websearch-on", "websearch-settings", "websearch-model"],
            "description": _("Websearch settings"),
        },
        "rag": {
            "title": _("RAG"),
            "settings": ["rag-on", "rag-model", "rag-settings", "rag-on-documents", "documents-context-limit"],
            "description": _("Document analyzer settings"),
        },
        "extensions": {
            "title": _("Extensions"),
            "settings": ["extensions-settings"],
            "description": _("Extensions settings"),
        },
        "interface": {
            "title": _("Inteface"),
            "settings": ["hidden-files", "reverse-order", "display-latex", "external-terminal-on", "external-terminal", "zoom","send-on-enter", "initial-browser-page", "external-browser", "browser-search-string", "browser-session-persist", "edit-color-scheme"],
            "description": _("Interface settings, hidden files, reverse order, zoom..."),
        },
        "general": {
            "title": _("General"),
            "settings": ["virtualization", "offers", "memory", "remove-thinking", "auto-generate-name", "path", "auto-run", "max-run-times",],
            "description": _("General settings, virtualization, offers, memory length, automatically generate chat name, current folder..."),
        },
        "prompts": {
                "title": _("Prompts"),
                "settings": ["prompts-settings", "custom-extra-prompt", "custom-prompts", "smart-prompt", "smart-prompt-settings", "smart-prompt-on"],
                "description": _("Prompts settings, custom extra prompt, custom prompts..."),
        }

}
