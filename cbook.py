import pickle

class Node:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.next = None

class ContactBook:
    def __init__(self):
        self.head = None

    def insert(self, name, phone, email):
        newNode = Node(name, phone, email)
        if self.head is None or name.lower() < self.head.name.lower():
            newNode.next = self.head
            self.head = newNode
            return
        cur = self.head
        while cur.next and cur.next.name.lower() < name.lower():
            cur = cur.next
        newNode.next = cur.next
        cur.next = newNode

    def search(self, name):
        cur = self.head
        while cur:
            if cur.name.lower() == name.lower():
                return cur
            cur = cur.next
        return None

    def update(self, name, phone=None, email=None):
        cur = self.search(name)
        if cur:
            if phone: cur.phone = phone
            if email: cur.email = email
            return True
        return False

    def delete(self, name):
        if not self.head: return False
        if self.head.name.lower() == name.lower():
            self.head = self.head.next
            return True
        cur = self.head
        while cur.next:
            if cur.next.name.lower() == name.lower():
                cur.next = cur.next.next
                return True
            cur = cur.next
        return False

    def show(self):
        cur = self.head
        if not cur:
            print("No contacts\n")
            return
        while cur:
            print(cur.name, "-", cur.phone, "-", cur.email)
            cur = cur.next

    def save(self, file="contacts.dat"):
        data = []
        cur = self.head
        while cur:
            data.append((cur.name, cur.phone, cur.email))
            cur = cur.next
        with open(file, "wb") as f:
            pickle.dump(data, f)

    def load(self, file="contacts.dat"):
        try:
            with open(file, "rb") as f:
                data = pickle.load(f)
                self.head = None
                for name, phone, email in sorted(data, key=lambda x: x[0].lower()):
                    self.insert(name, phone, email)
        except:
            pass

def main():
    book = ContactBook()
    book.load()
    while True:
        print("\n1 Add  2 Show  3 Search  4 Update  5 Delete  6 Save&Exit")
        ch = input("Choice: ")
        if ch == "1":
            n = input("Name: ")
            p = input("Phone: ")
            e = input("Email: ")
            book.insert(n, p, e)
        elif ch == "2":
            book.show()
        elif ch == "3":
            n = input("Name to search: ")
            c = book.search(n)
            if c: print(c.name, "-", c.phone, "-", c.email)
            else: print("Not found")
        elif ch == "4":
            n = input("Name to update: ")
            p = input("New Phone (enter to skip): ")
            e = input("New Email (enter to skip): ")
            if book.update(n, p if p else None, e if e else None):
                print("Updated")
            else:
                print("Not found")
        elif ch == "5":
            n = input("Name to delete: ")
            if book.delete(n): print("Deleted")
            else: print("Not found")
        elif ch == "6":
            book.save()
            print("Saved. Bye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
