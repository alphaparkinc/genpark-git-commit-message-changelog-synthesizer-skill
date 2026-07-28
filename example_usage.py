from client import GitChangelogClient

def main():
    client = GitChangelogClient()
    res = client.synthesize_changelog(diff='+ feat: add auth')
    print(f"Result for changelog_md: {res['changelog_md']}")

if __name__ == "__main__":
    main()
