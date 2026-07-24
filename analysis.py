def analyze_pair(pair):
    pair = pair.upper()

    analysis = {
        "EURUSD": {
            "trend": "Bullish",
            "entry": "Waiting for confirmation",
            "stop_loss": "Not set",
            "take_profit": "Not set"
        },
        "GBPUSD": {
            "trend": "Bearish",
            "entry": "Waiting for confirmation",
            "stop_loss": "Not set",
            "take_profit": "Not set"
        },
        "XAUUSD": {
            "trend": "Bullish",
            "entry": "Waiting for confirmation",
            "stop_loss": "Not set",
            "take_profit": "Not set"
        }
    }

    if pair in analysis:
        return analysis[pair]

    return {
        "trend": "Unknown",
        "entry": "N/A",
        "stop_loss": "N/A",
        "take_profit": "N/A"
    }