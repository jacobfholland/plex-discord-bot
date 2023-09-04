import logging

from run import plex


def active_sessions():
    # TODO: Formatting looks bad
    active_sessions = plex.sessions()
    if active_sessions:
        logging.warning("Clients currently playing something:")
        for session in active_sessions:
            client_name = session.players[0].title if session.players else "Unknown"
            media_title = session.title if session.title else "Unknown"
            logging.warning(
                f"""
Client: {client_name},
Media: {media_title})
Machine Identifier: {session.player.machineIdentifier}
\n
"""
            )
    else:
        logging.warning("No clients currently playing.")
