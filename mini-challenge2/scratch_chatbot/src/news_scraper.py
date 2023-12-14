import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import json
import random
import os


def scrape_srf_links(url, topic=None):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all anchor tags (a) with an 'href' attribute
        links = soup.find_all("a", href=True)

        # Initialize a list to store links for the specified topic
        topic_links = []

        # Initialize a set to store unique topics
        possible_topics = set()

        # Categorize and format the URLs into the list for the specified topic
        for link in links:
            formatted_url = urljoin(url, link["href"])
            topics = re.findall(r"/([^/]+)/", formatted_url)
            for t in topics:
                possible_topics.add(t)
            if topic and f"/{topic}" in formatted_url:
                topic_links.append(formatted_url)

        if topic:
            return topic_links
        else:
            return possible_topics

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None


# To get all possible topics
# print(list(scrape_srf_links("https://www.srf.ch")))

# To get links related to a specific topic (e.g., "sport")
# print(scrape_srf_links("https://www.srf.ch", "sport"))


def get_data_for_topics(topics, data_directory="data/"):
    # Initialize a dictionary to store data for all topics
    combined_data = {"intents": []}

    for topic in topics:
        # Call the existing function to scrape links
        topic_links = scrape_srf_links("https://www.srf.ch", topic)

        # Check if links were successfully retrieved
        if topic_links:
            # Prepare the JSON structure for the current topic
            topic_data = {
                "tag": topic.replace("_", " "),
                "patterns": [
                    f"Get me the latest {topic.replace('_', ' ')}",
                    f"Tell me about {topic.replace('_', ' ')}",
                    f"What's happening in {topic.replace('_', ' ')}",
                    f"Give me updates on {topic.replace('_', ' ')}",
                    f"I'm interested in {topic.replace('_', ' ')}",
                    f"Can you provide {topic.replace('_', ' ')} ",
                    f"Tell me more about {topic.replace('_', ' ')}",
                    f"Share {topic.replace('_', ' ')}",
                    f"{topic.replace('_', ' ')}",
                ],
                "responses": [],
            }

            # Add a response for each link
            for link in topic_links:
                response_variations = [
                    f"Here is a {topic.replace('_', ' ')} news article: {link}",
                    f"Here's some {topic.replace('_', ' ')} news for you: {link}",
                    f"Check out this {topic.replace('_', ' ')} news: {link}",
                    f"Here's the latest {topic.replace('_', ' ')} news: {link}",
                    f"Sure, here's a {topic.replace('_', ' ')} news link: {link}",
                    f"{topic.replace('_', ' ')} news coming right up: {link}",
                    f"Here you go, the {topic.replace('_', ' ')} news you requested: {link}",
                    f"Enjoy this {topic.replace('_', ' ')} news article: {link}",
                ]
                response = random.choice(response_variations)
                topic_data["responses"].append(response)

            # Add the data for the current topic to the combined_data
            combined_data["intents"].append(topic_data)
        else:
            print(f"No links found for the topic {topic}. Skipping.")

    # Specify the full path to the combined JSON file
    combined_filename = "intents_news.json"
    combined_full_path = os.path.join(data_directory, combined_filename)

    # Write the combined data to the JSON file
    with open(combined_full_path, "w") as json_file:
        json.dump(combined_data, json_file, indent=4)

    print(
        f"Combined JSON file '{combined_full_path}' created successfully for all topics."
    )


# topics_list = list(scrape_srf_links("https://www.srf.ch"))

# get_data_for_topics(topics_list)
