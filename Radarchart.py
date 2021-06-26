import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-dark')
categories = ['Damage','Fire Rate', 'Accuracy', 'Mobility'	,'Range']
categories = [*categories,categories[0]]

AK47 = [70,55,45,60,65]
MP5 = [40,83,40,80,49]
M4LMG = [46,63,61,44,64]
KAR98 = [81,28,70,49,86]

AK47 = [*AK47,AK47[0]]
MP5 = [*MP5,MP5[0]]
M4LMG = [*M4LMG,M4LMG[0]]
KAR98 = [*KAR98,KAR98[0]]

label_loc = np.linspace(start=0, stop=2*np.pi, num=len(AK47))

plt.figure(figsize=(6,6))
plt.subplot(polar=True)

plt.plot(label_loc, AK47)
plt.plot(label_loc, MP5)
plt.plot(label_loc, M4LMG)
plt.plot(label_loc, KAR98)

plt.fill(label_loc, AK47, 'blue', alpha=0.1)
plt.legend(['AK47','MP5','M4LMG','KAR98'],loc=(0.95,0.8))

plt.title('Guns Comparison',size='18')
lines, labels = plt.thetagrids(np.degrees(label_loc),labels=categories)
plt.show()