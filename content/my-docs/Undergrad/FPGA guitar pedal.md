> *Disclaimer:* I did not document my undergrad work very well back in the day. So this page is describing what I was able to find from 2022.

## **Introduction**

This project leverages an FPGA-based System-on-Chip (SoC) featuring both a Hard Processor Core (HPC) and a softcore processor. It is designed to configure and optimize chains of digital signal processing (DSP) effects for electric guitar performance.

DE 10 board
---
![[Pasted image 20241119172002.png]]
### **Cyclone V SoC**

The Cyclone V SoC features 110K logic units dedicated to hardware effects. It is fully compatible with the NIOS II softcore processor, providing flexibility for custom implementations.

---

### **ARM Cortex-A9 Dual Core**

While the ARM Cortex-A9 Dual Core is integrated as the Hard Processor System (HPS), the system will primarily rely on the NIOS II softcore processor. The HPS will remain available for potential stretch goals or extended functionality.

---

### **NIOS II Softcore Processor**

The NIOS II processor will replace the HPS in this system due to its seamless integration with FPGA IP cores. This approach simplifies development and enables experimentation with processor specifications, such as clock speed and RAM/ROM configurations, to optimize performance for specific use cases.

### Guitar pedal project PDF

![[guitar_pedal.pdf]]