---
schema: qual/card@1
id: P-O7DMP
kind: problem
title: "Define $\\begin{aligned}F(x) &\\da \\qty{ \\sin(\\pi x) \\over \\pi x}^2 \\\\ G(x) &\\da \\begin{cases} 1 - \\abs{x} & \\abs{x} \\leq 1 \\\\ 0 & \\text{else}. \\end{cases}\\end{aligned}$ Show that $\\fourier{G}(\\xi) = F(\\xi)$"
classification:
  areas:
  - real-analysis
  topics:
  - fourier-analysis
  - integrals
relations: []
review: draft
---
Define
\[
F(x) &\da \qty{ \sin(\pi x) \over \pi x}^2 \\
G(x) &\da 
\begin{cases}
1 - \abs{x} & \abs{x} \leq 1
\\
0 & \text{else}.
\end{cases}
\]

a. Show that $\fourier{G}(\xi) = F(\xi)$

b. Compute $\fourier{F}$.

c. Give an example of a function $g\not \in L^1(\RR)$ which is the Fourier transform of an $L^1$ function.

*Hint: write \( \fourier{G}(\xi) = H(\xi) + H(-\xi) \)  where*
\[
H(\xi) \da e^{2\pi i \xi} \int_0^1 y e^{2\pi i y \xi }\dy 
.\]
