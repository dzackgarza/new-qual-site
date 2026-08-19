---
schema: qual/card@1
id: S-BO7IN
kind: solution
title: Solution to P-8XT77
classification:
  areas:
  - real-analysis
  topics:
  - dual-spaces
  - functional-analysis
  - weak-convergence
relations:
- kind: solves
  target: P-8XT77
review: draft
---

:::{.solution}
We claim that $\overline{S_{X^*}}$ in the $w^*$ topology is $\text{Ball}_{X^*}$. Indeed, at first, if $\|x^*\|>1$, then there is a $x\in X$ such that $\|x\|=1$ and $|x^*(x)|>1$. Then, there is an $\epsilon$ such that the nbhd of $x^*$, $A=\{y^*:|x^*(x)-y^*(x)|<\epsilon\}$ does not intersect with $\text{Ball}_{X^*}$. To see this, for all $y^*\in A$, $|y^*(x)|>1$ and thus $\|y^*\|>1$.

Then, fix a $x^*$ with $\|x^*\|\le 1$. Consider a general nbhd of $x^*$, say $O=\bigcap_{i=1}^n\{y^*:|x^*(x_i)-y^*(x_i)|<\epsilon\}$. Let $M=\text{span}\{x_i:i=1,\dots,n\}$. To simplify the notation, we denote $\phi$ for $x^*$. Let $H_\phi=\{f\in X^*:f|_M=\phi\}$. We claim that $H_\psi$ is weak*-closed, convex and nonempty set.

Indeed, any Hahn-Banach extension of $\phi$, say, $f$ with $\|f\|=\|\psi\|\le 1$ implies that $H_\phi$ is nonempty. For all $f_1,f_2\in H_\phi$, $0<\lambda<1$, $\lambda f_1+(1-\lambda)f_2|_M=\phi$ and $\|\lambda f_1+(1-\lambda)f_2\|\le 1$. Thus, $H_\phi$ is convex. Now, let $f_\mu(x)\to f(x)$ for all $x\in X$, where $f_\mu\in H_\phi$. Then since $f_\mu|_M=\phi$, $f|_M=\phi$. In addition, for all $x$ is of norm 1, $|f_\mu(x)|\le\|f_\mu\|\|x\|\le 1$. This implies that $|f(x)|\le 1$ and thus $\|f\|\le 1$, which implies that $H_\phi$ is $w^*$-closed.

Then, by Krein-Milman theorem, $\text{Ext}(H_\phi)\ne\varnothing$. Let $f\in\text{Ext}(H_\phi)$, we claim that $\|f\|=1$. Indeed, suppose $\|f\|<1$. Let $g$ be a linear functional, such that $g|_M=0$ but $\|g\|=1$. Then define $f_1=f+(1-\|f\|)g$ and $f_2=f-(1-\|f\|)g$. Then, it can be verified that $\|f_1\|\le 1$, $\|f_2\|\le 1$ and $f_1|_M=f_2|_M=\phi$. However, $f=(f_1+f_2)/2$. This contradicts to $f\in\text{Ext}(H_\phi)$. Thus, $f\in S_{X^*}\cap O$. We are done.
:::
