
# coding: utf-8

# In[1]:


def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo',age=3)

