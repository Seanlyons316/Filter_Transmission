#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy as np
import matplotlib.pyplot as plt

file_path = 'LED data\LED_2.txt'

try:
    with open(file_path, 'r') as f:
        data = [i.split() for i in f.readlines()]
except PermissionError:
    print(f"Permission denied: Cannot access '{file_path}'. Try running as admin or checking file permissions.")
except FileNotFoundError:
    print(f"File not found: '{file_path}'. Ensure the path is correct.")
    
no_filter = 'LED data\LED_6.txt'

try:
    with open(no_filter, 'r') as f:
        data_no_filter = [i.split() for i in f.readlines()]
except PermissionError:
    print(f"Permission denied: Cannot access '{file_path}'. Try running as admin or checking file permissions.")
except FileNotFoundError:
    print(f"File not found: '{file_path}'. Ensure the path is correct.")



# In[44]:


print(data)


# In[45]:


print(data_no_filter)


# In[64]:


if data is not None and data_no_filter is not None:
    data = np.array(data, dtype=float)
    data_no_filter = np.array(data_no_filter, dtype=float)

    wavelength = data_no_filter[:, 0]
    intensity_filtered = data[:, 1]
    intensity_no_filter = data_no_filter[:, 1]
    
    # Create a mask that removes rows where either intensity is zero
    valid_mask = (intensity_no_filter > 0) & (intensity_filtered > 0.1)

    # Apply mask to remove zero entries
    wavelength = wavelength[valid_mask]
    intensity_no_filter = intensity_no_filter[valid_mask]
    intensity_filtered = intensity_filtered[valid_mask]

    
    transmission = np.divide(intensity_no_filter, intensity_filtered)

    print("Transmission values:", transmission)  


# In[65]:


len(transmission)


# In[66]:


len(wavelength)


# In[67]:


plt.figure(figsize=(8, 5))
plt.plot(wavelength, transmission, label="Transmission Function", color='b', marker='o', linestyle='-')

    # Labels and title
plt.xlabel("Wavelength (nm)")
plt.ylabel("Transmission")
plt.title("Transmission Function vs. Wavelength")
plt.legend()
plt.grid(True)
plt.show()

#try adjusting the bin sizing to maybe condense the plot


# In[ ]:




