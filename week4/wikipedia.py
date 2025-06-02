import sys
import collections
from collections import deque

class Wikipedia:

    # Initialize the graph of pages.
    def __init__(self, pages_file, links_file):

        # A mapping from a page ID (integer) to the page title.
        # For example, self.titles[1234] returns the title of the page whose
        # ID is 1234.
        self.titles = {}

        # A set of page links.
        # For example, self.links[1234] returns an array of page IDs linked
        # from the page whose ID is 1234.
        self.links = {}

        # Read the pages file into self.titles.
        with open(pages_file) as file:
            for line in file:
                (id, title) = line.rstrip().split(" ")
                id = int(id)
                assert not id in self.titles, id
                self.titles[id] = title
                self.links[id] = []
        print("Finished reading %s" % pages_file)


        # Read the links file into self.links.
        with open(links_file) as file:
            for line in file:
                (src, dst) = line.rstrip().split(" ")
                (src, dst) = (int(src), int(dst))
                assert src in self.titles, src
                assert dst in self.titles, dst
                self.links[src].append(dst)
        print("Finished reading %s" % links_file)
        print()


    # Find the longest titles. This is not related to a graph algorithm at all
    # though :)
    def find_longest_titles(self):
        titles = sorted(self.titles.values(), key=len, reverse=True)
        print("The longest titles are:")
        count = 0
        index = 0
        while count < 15 and index < len(titles):
            if titles[index].find("_") == -1:
                print(titles[index])
                count += 1
            index += 1
        print()


    # Find the most linked pages.
    def find_most_linked_pages(self):
        link_count = {}
        for id in self.titles.keys():
            link_count[id] = 0

        for id in self.titles.keys():
            for dst in self.links[id]:
                link_count[dst] += 1

        print("The most linked pages are:")
        link_count_max = max(link_count.values())
        for dst in link_count.keys():
            if link_count[dst] == link_count_max:
                print(self.titles[dst], link_count_max)
        print()


    # Find the shortest path.
    # |start|: The title of the start page.
    # |goal|: The title of the goal page.
    def find_shortest_path(self, start, goal):
        start_id = None
        goal_id = None

    # get the ID of star and goal
        for page_id, page_title in self.titles.items():
            if page_title == start:
                start_id = page_id
            elif page_title == goal:
                goal_id = page_id

    # continue if both start and goal exist
        if start_id is not None and goal_id is not None:
            distances = {start_id: 0} 
            predecessors = {start_id: None}
            queue = deque() #make deque object
            queue.append(start_id)  # enqueue

            while queue:
                current_page = queue.popleft()  # delete one element from the top (left side) and return its value. (dequeue)

                # if we get to the goal, restore the route and return the path
                if current_page == goal_id:
                    path = self.reconstruct_path(predecessors, goal_id)
                    path_titles = [self.titles[page_id] for page_id in path]
                    print(path_titles)
                    return 0
                

                for neighbor in self.links[current_page]:
                    if neighbor not in distances:  # if the node has not yet been reached
                        distances[neighbor] = distances[current_page] + 1
                        predecessors[neighbor] = current_page
                        queue.append(neighbor) # queue it as the next node to be explored

        # if we cannot find the way from start to goal
        print("[]")

    def reconstruct_path(self, predecessors, goal):
        path = [goal]
        current = goal
        while predecessors[current] is not None:
            current = predecessors[current]
            path.append(current)
        path.reverse()
        return path

    
    def make_current_pagerank(self):
        keys_list = list(self.titles.keys())
        keys_set = set(keys_list)
        max_keys = max(keys_list)
        current_pagerank = []
        i = 0
        for i in range(max_keys + 1):
            if i in keys_set:
                current_pagerank.append({"ID": i, "value": 1 })
            else:
                current_pagerank.append({"ID": i, "value": 0 })
        return current_pagerank

    def make_new_pagerank(self):
        keys_list = list(self.titles.keys())
        max_keys = max(keys_list)
        new_pagerank = []
        for i in range(max_keys + 1):
            new_pagerank.append({"ID": i, "value": 0 })
        return new_pagerank

    # Calculate the page ranks and print the most popular pages.
    def find_most_popular_pages(self,count):
        length = len(self.titles)
        counter = 0
        keys_list = list(self.titles.keys())
        current_pagerank = self.make_current_pagerank()

        while counter < count:
            sum = 0
            total_score2 = 0
            new_pagerank = self.make_new_pagerank()
            # calculate scores
            for i in keys_list:
                if len(self.links[i]) == 0:
                    score2 = current_pagerank[i]["value"] / (length - 1)
                    total_score2 += score2
                else:
                    score = current_pagerank[i]["value"] * 0.85 / len(self.links[i])
                    score2 = current_pagerank[i]["value"] * 0.15 / (length - 1)
                    for links in self.links[i]:
                        new_pagerank[links]["value"] += score
                        sum += score
                    total_score2 += score2
                    new_pagerank[i]["value"] -= score2
                    sum -= score2
            for i in keys_list:
                new_pagerank[i]["value"] += total_score2
                sum += total_score2
            # for check
            print("sum:",sum)
            current_pagerank = new_pagerank
            counter += 1

        sorted_rank = sorted(current_pagerank, key = lambda x: x["value"], reverse=True)
        for key in sorted_rank[:10]:
            print(key)




    # Do something more interesting!!
    def find_something_more_interesting(self):
        #------------------------#
        # Write your code here!  #
        #------------------------#
        pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: %s pages_file links_file" % sys.argv[0])
        exit(1)

    wikipedia = Wikipedia(sys.argv[1], sys.argv[2])
    wikipedia.find_longest_titles()
    wikipedia.find_most_linked_pages()
    wikipedia.find_shortest_path("渋谷", "パレートの法則")
    wikipedia.find_shortest_path("アンパサンド", "プログラミング言語")
    wikipedia.find_most_popular_pages(10)
