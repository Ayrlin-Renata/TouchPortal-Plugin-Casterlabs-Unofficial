# Version string of this plugin (in Python style).
__version__ = "1.0"

# The unique plugin ID string is used in multiple places.
# It also forms the base for all other ID strings (for states, actions, etc).
PLUGIN_ID = "tp.plugin.ayrlin.tpcasterlabs-unofficial"

# Basic plugin metadata
TP_PLUGIN_INFO = {
    "sdk": 6,
    "version": int(float(__version__) * 100),  # TP only recognizes integer version numbers
    "name": "Casterlabs Unofficial",
    "id": PLUGIN_ID,
    # Startup command, with default logging options read from configuration file (see main() for details)
    "plugin_start_cmd": "%TP_PLUGIN_FOLDER%TouchPortalCasterlabsUnofficial\\tpcasterlabs-unofficial.exe",
    "configuration": {
        "colorDark": "#25274c",
        "colorLight": "#707ab5"
    },
    "doc": {
        "repository": "Ayrlin-Renata:TouchPortal-Plugin-Casterlabs-Unofficial",
        "Install": "git gud",
        "description": "websocket for local casterlabs events to translate to touchportal events"
    }
}

# Setting(s) for this plugin. These could be either for users to
# set, or to persist data between plugin runs (as read-only settings).
TP_PLUGIN_SETTINGS = {
    "Authorization": {
        "name": "Authorization",
        "type": "text",
        "default": "",
        "readOnly": False,  # this is also the default
        "doc": "authorization string",
        "isPassword": True
    },
    "FollowId": {
        "name": "FollowId",
        "type": "text",
        "default": "",
        "readOnly": False,  # this is also the default
        "doc": "widget identification",
        "isPassword": False
    },
    "SubscribeId": {
        "name": "SubscribeId",
        "type": "text",
        "default": "",
        "readOnly": False,  # this is also the default
        "doc": "widget identification",
        "isPassword": False
    },
    "RaidId": {
        "name": "RaidId",
        "type": "text",
        "default": "",
        "readOnly": False,  # this is also the default
        "doc": "widget identification",
        "isPassword": False
    },
}

# This example only uses one Category for actions/etc., but multiple categories are supported also.
TP_PLUGIN_CATEGORIES = {
    "main": {
        "id": PLUGIN_ID + ".main",
        "name" : "Casterlabs",
        # "imagepath" : "icon-24.png"
    }
}

# Action(s) which this plugin supports.
TP_PLUGIN_ACTIONS = {
    # "example": {
    #     # "category" is optional, if omitted then this action will be added to all, or the only, category(ies)
    #     "category": "main",
    #     "id": PLUGIN_ID + ".act.example",
    #     "name": "Set Example Action",
    #     "prefix": TP_PLUGIN_CATEGORIES["main"]["name"],
    #     "type": "communicate",
    #     "tryInline": True,
    #     "doc": "Example doc for this action in readme",
    #     # "format" tokens like $[1] will be replaced in the generated JSON with the corresponding data id wrapped with "{$...$}".
    #     # Numeric token values correspond to the order in which the data items are listed here, while text tokens correspond
    #     # to the last part of a dotted data ID (the part after the last period; letters, numbers, and underscore allowed).
    #     "format": "Set Example State Text to $[text] and Color to $[2]",
    #     "data": {
    #         "text": {
    #             "id": PLUGIN_ID + ".act.example.data.text",
    #             # "text" is the default type and could be omitted here
    #             "type": "text",
    #             "label": "Text",
    #             "default": "Hello World!"
    #         },
    #         "color": {
    #             "id": PLUGIN_ID + ".act.example.data.color",
    #             "type": "color",
    #             "label": "Color",
    #             "default": "#818181FF"
    #         },
    #     }
    # },
}

TP_PLUGIN_CONNECTORS = {}

# Plugin static state(s). These are listed in the entry.tp file,
# vs. dynamic states which would be created/removed at runtime.
TP_PLUGIN_STATES = {
    "cl.newfollower": {
        "category": "main",
        # "parentGroup": "Follow",
        "id": PLUGIN_ID + ".state.cl.newfollower",
        "type": "choice",
        "valueChoices": [
            "New",
            "Waiting"
        ],
        "desc": "New Follower",
        "doc": "'New' or 'Waiting'",
        "default": "Waiting"
    },
    "cl.lastfollowername": {
        "category": "main",
        # "parentGroup": "Follow",
        "id": PLUGIN_ID + ".state.cl.lastfollowername",
        "type": "text",
        "desc": "Last Follower Name",
        "default": "name-fetch-error-try-adding-delay-lmao-sry"
    },
    "cl.newsubscriber": {
        "category": "main",
        # "parentGroup": "Follow",
        "id": PLUGIN_ID + ".state.cl.newsubscriber",
        "type": "choice",
        "valueChoices": [
            "New",
            "Waiting"
        ],
        "desc": "New Subscriber",
        "doc": "'New' or 'Waiting'",
        "default": "Waiting"
    },
    "cl.lastsubscribername": {
        "category": "main",
        # "parentGroup": "Follow",
        "id": PLUGIN_ID + ".state.cl.lastsubscribername",
        "type": "text",
        "desc": "Last Subscriber Name",
        "default": "name-fetch-error-try-adding-delay-lmao-sry"
    },
    "cl.newraid": {
        "category": "main",
        # "parentGroup": "Follow",
        "id": PLUGIN_ID + ".state.cl.newraid",
        "type": "choice",
        "valueChoices": [
            "New",
            "Waiting"
        ],
        "desc": "New Raid",
        "doc": "'New' or 'Waiting'",
        "default": "Waiting"
    },
    "cl.lastraidname": {
        "category": "main",
        # "parentGroup": "Follow",
        "id": PLUGIN_ID + ".state.cl.lastraidname",
        "type": "text",
        "desc": "Last Raid Name",
        "default": "name-fetch-error-try-adding-delay-lmao-sry"
    },
}

# Plugin Event(s).
TP_PLUGIN_EVENTS = {
    # "cl.follow": {
    #     "id": "event.cl.follow",
    #     "name": "On Followed",
    #     "format": "When the new follower state is $val",
    #     "type": "communicate",
    #     "valueType": "choice",
    #     "valueChoices": [
    #         "New",
    #         "Waiting"
    #     ],
    #     "valueStateId": "cl.newfollower"
    # }
}