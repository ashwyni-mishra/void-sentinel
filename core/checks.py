import discord

def has_permission(member: discord.Member, perm: str) -> bool:
    """
    Check if the member has a specific permission.
    Example: has_permission(user, "ban_members")
    """
    return getattr(member.guild_permissions, perm, False)


def require_perm(member: discord.Member, perm: str):
    """
    Return an error message if the member lacks the permission.
    """
    if not has_permission(member, perm):
        return f"❌ You need **{perm.replace('_', ' ').title()}** permission to use this command."
    return None
