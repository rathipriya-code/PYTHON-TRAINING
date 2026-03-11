from ddgs import DDGS

print("Searching...")

query = "Learning Python OOPS concept"

with DDGS() as ddgs:
    results = ddgs.text(query, max_results=10)

    for r in results:
        print(r["title"])
        print(r["href"])
        print()
