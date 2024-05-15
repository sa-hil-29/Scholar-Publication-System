from serpapi.google_search import GoogleSearch
import json

def get_faculty_papers_by_email(email):
    print(email)
    params = {
        "engine": "google_scholar",
        "q": email,
        "api_key": "a47db9b3899471d7aabb29628737a9ac9cf8e19bc8a6f8dd6da18e2994b385b6"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    print(json.dumps(results, indent = 4))
    
    return results

def get_author_id(author,email):
    result = get_faculty_papers_by_email(email)
    
    for i in range(len(result["organic_results"])):
        authors = result["organic_results"][i]["publication_info"]["authors"]
        for publication in result["organic_results"]:
            print(json.dumps(publication, indent=4))
            for i in range(len(authors)):
                if authors[i]["name"] == author:
                    # print(authors[i]["name"])
                    return authors[i]["author_id"]

def get_papers_by_author_id(email,author):
    author_id = get_author_id(author,email)
    
    params = {
        "engine": "google_scholar_author",
        "author_id": author_id,
        "api_key": "a47db9b3899471d7aabb29628737a9ac9cf8e19bc8a6f8dd6da18e2994b385b6"
    }
    search = GoogleSearch(params)
    result = search.get_dict()
    
    print(json.dumps(result, indent=4))
    return result