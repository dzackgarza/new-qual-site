---
schema: qual/card@1
id: P-MOL6S
kind: problem
title: "1. Denoting $D^n f \\definedas \\dd{^n f}{x^n}$ and noting that $D^1 D^n\u2026"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---
1. Denoting $D^n f \definedas \dd{^n f}{x^n}$ and noting that $D^1 D^n f = D^{n+1}f$, we have
  $$\begin{align*}
  D^0f &= xe^{2x} \\
  D^1f &= e^{2x} + 2D^0f \\
  D^2f &= 2e^{2x} + 2D^1f \\
  D^3f &= 4e^{2x} + 2D^2f \\
  \end{align*}$$

    and (claim) so we find that 
  $$D^n f = 2^{n-1}e^{2x} + 2D^{n-1}f.$$
  
    This is trivially the case for $n=1$, where we've computed $D^1 f = e^2x + 2xe^{2x} = 2^0e^{2x} + 2D^0 f$, and the inductive step holds exactly because 
  $$
  D^{n+1}f = DD^{n}f \\
  = D(2^{n-1}e^{2x} + 2D^{n-1}f) \\
  =2^n e^{2x} + 2D^n f.
  $$
  $\qed$

