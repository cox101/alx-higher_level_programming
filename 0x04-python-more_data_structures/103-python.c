#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
void print_python_list(PyObject *p) {
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (Py_ssize_t i = 0; i < PyList_Size(p); ++i) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    printf("[.] Python bytes info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  Size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AS_STRING(p));

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; ++i) {
        printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
        if (i + 1 < PyBytes_Size(p) && i + 1 < 10)
            printf(" ");
    }
    printf("\n");
}
