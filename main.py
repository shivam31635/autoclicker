import time

def main():
    # Click on the link
    click("https://shareus.io/0cGhFo")
    # Wait for 5 seconds
    time.sleep(5)
    # Find the article link
    article_link = find_element_by_xpath("//a[contains(@href, 'https://paid.outbrain.com')]")
    # Click on the article link
    click(article_link)
    # Wait for 15 seconds
    time.sleep(15)
    # Go back
    back()
    # Click on the open link button
    click("//button[contains(@text, 'Open Link')]")
    # Go back
    back()
    # Go to the article
    click(article_link)
    # Go back
    back()

    # Repeat the process
    while True:
        main()

if __name__ == "__main__":
    main()
