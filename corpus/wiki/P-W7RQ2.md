---
schema: qual/card@1
id: P-W7RQ2
kind: problem
title: "Show that for each \\( \\epsilon>0 \\) the following function is the Four\u2026"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Show that for each \( \epsilon>0 \) the following function is the Fourier transform of an $L^1(\RR^n)$ function:
\[
F(\xi) \da \qty{1 \over 1 + \abs{\xi}^2}^{\epsilon}
.\]


*Hint: show that*

\[
K_\delta(x) &\da \delta^{-n/2} e^{-\pi \abs{x}^2 \over \delta} \\
f(x) &\da \int_0^{\infty } K_{\delta}(x) e^{-\pi \delta} \delta^{\epsilon - 1} \,d \delta \\
\Gamma(s) &\da \int_0^{\infty } e^{-t} t^{s-1} \dt \\
\implies \fourier{f}(\xi) &= \int_0^{\infty } e^{- \pi \delta \abs{\xi}^2} e^{ -\pi \delta} \delta^{\epsilon - 1}
= \pi^{-s} \Gamma(\epsilon) F(\xi)
.\]
