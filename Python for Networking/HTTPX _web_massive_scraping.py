import asyncio
import json
import time

import httpx
import xmltojson

json_result=None
async def fetch():
    urls=["https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html",
    "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-2.html",
    "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-3.html",
    "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-4.html",
    "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-5.html",
    "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-6.html",
    "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html",
     "https://books.toscrape.com/catalogue/category/books/fiction_10/page-2.html",
      "https://books.toscrape.com/catalogue/category/books/fiction_10/page-3.html",
       "https://books.toscrape.com/catalogue/category/books/fiction_10/page-4.html",
    ]
    urls1=["https://geeksforgeeks-example.surge.sh"]

    async with httpx.AsyncClient() as client:
        reqs=[client.get(url) for url in urls]
        results=await asyncio.gather(*reqs)
    print (results)

    async with httpx.AsyncClient() as client:
        reqs=[client.get(url) for url in urls1]
        results1=await asyncio.gather(*reqs)
    # take first book content html
    data=results1[0].text #xml content

    # Save the page content as sample.html
    with open("sample.html", "w") as html_file:
        html_file.write(data)

    with open("sample.html", "r") as html_file:
        html = html_file.read()
        json_ = xmltojson.parse(html)

    with open("data.json", "w") as file:
        json.dump(json_, file)

    print(json_)


start=time.perf_counter()
asyncio.run(fetch())
end=time.perf_counter()

print(f'time elapsed to fetch data is: {end-start}')
