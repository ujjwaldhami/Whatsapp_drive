def parse_command(command: str) -> str:
    command = command.strip().upper()

    if command.startswith("LIST"):
        folder = command[5:]
        return f"📁 Listing files in: {folder}"
    elif command.startswith("DELETE"):
        file = command[7:]
        return f"🗑️ Deleting: {file}"
    elif command.startswith("MOVE"):
        args = command[5:].split()
        if len(args) == 2:
            return f"📂 Moving {args[0]} → {args[1]}"
        else:
            return "❌ Usage: MOVE <file> <destination>"
    elif command.startswith("SUMMARY"):
        folder = command[8:]
        return f"📝 Generating summary for: {folder}"
    else:
        return "❓ Unknown command"
