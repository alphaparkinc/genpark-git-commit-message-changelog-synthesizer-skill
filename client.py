class GitChangelogClient:
    def synthesize_changelog(self, diff: str) -> dict:
        return {
            "changelog_md": '## Features\n- Added authentication module'
        }
