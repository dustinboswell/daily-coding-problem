// g++ -std=c++11 -Wall xor_list.cpp -o xor_list
#include <cassert>
#include <cstdint>

template<class T>
struct Node {
    T element;
    Node* both;
};

template<typename T>
T* xor_pointers(T* a, T* b) {
    return reinterpret_cast<T*>(reinterpret_cast<uintptr_t>(a) ^ reinterpret_cast<uintptr_t>(b));
}

template<class T>
class XorList {
    Node<T>* head = nullptr;
  public:
    void add(const T& element) {
        if (head == nullptr) {
            head = new Node<T>();
            head->element = element;
            head->both = nullptr;
            return;
        }
        Node<T>* prev = nullptr;
        Node<T>* cur = head;
        while (Node<T>* next = xor_pointers(cur->both, prev)) {
            prev = cur;
            cur = next;
        }
        Node<T>* new_node = new Node<T>();
        new_node->both = cur;
        new_node->element = element;
        cur->both = xor_pointers(cur->both, new_node);
    }

    const T& get(int index) {
        // assume index is valid
        Node<T>* prev = nullptr;
        Node<T>* cur = head;
        while (index) {
            Node<T>* next = xor_pointers(cur->both, prev);
            prev = cur;
            cur = next;
            index--;
        }
        return cur->element;
    }
};

int main() {
    XorList<char> list;
    list.add('a');
    assert(list.get(0) == 'a');
    list.add('b');
    assert(list.get(0) == 'a');
    assert(list.get(1) == 'b');
}
