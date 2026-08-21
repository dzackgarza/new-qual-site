---
schema: qual/card@1
id: P-LG4GL
kind: problem
title: $\left(\int\frac{|\phi|^n}{1+x^2}\,dx\right)^{1/n}\to\|\phi\|_\infty$
classification:
  areas:
  - real-analysis
  topics:
  - L∞
  - Lp Spaces
  - Limits
relations: []
review: draft
solved: true
---

Let $\phi\in L^\infty(\RR)$. Show that the following limit exists and satisfies the equality
\[
\lim _{n \to \infty} \left(\int _{\mathbb{R}} \frac{|\phi(x)|^{n}}{1+x^{2}} \, dx \right) ^ {\frac{1}{n}} 
= \norm{\phi}_\infty.
\]

:::{.solution}
\envlist
:::{.concept}
\envlist
- ?
:::

Let $L$ be the LHS and $R$ be the RHS.

Claim: $L\leq R$.
  - Since $\abs \phi \leq \norm{\phi}_\infty$ a.e., we can write 
  \[  
  L^{1\over n} 
  &\definedas \int_\RR { \abs{\phi(x)}^n \over 1+ x^2} \\
  &\leq \int_\RR { \norm{\phi}_\infty^n \over 1+ x^2}  \\
  &= \norm{\phi}_\infty^n \int_\RR {1\over 1 + x^2} \\
  &= \norm{\phi}_\infty^n \arctan(x)\evalfrom_{-\infty}^{\infty}  \\
  &= \norm{\phi}_\infty^n \qty{{\pi \over 2} - {-\pi \over 2} }  \\
  &= \pi \norm{\phi}_\infty^n \\ \\
  \implies L^{1\over n} &\leq \sqrt[n]{\pi \norm{\phi}_\infty^n} \\ 
  \implies L &\leq \pi^{1\over n} \norm{\phi}_\infty \\
  &\converges{n\to \infty }\to \norm{\phi}_\infty
  ,\]
  where we've used the fact that $c^{1\over n} \converges{n\to\infty}\to 1$ for any constant $c$.:::{.remark}
Actually true? Need conditions?
:::
  
Claim: $R\leq L$.

- We will show that $R\leq L + \eps$ for every $\eps>0$.
- Set 
\[  
S_\eps \definedas \theset{x\in \RR^n\suchthat \abs{\phi(x)} \geq \norm{\phi}_\infty - \eps}
.\]
- Then we have
\[  
\int_\RR {\abs{\phi(x)}^n \over 1 +x^2}\,dx
&\geq \int_{S_\eps} {\abs{\phi(x)}^n \over 1 +x^2}\,dx \quad S_\eps \subset \RR \\
&\geq \int_{S_\eps} { \qty{\norm{\phi}_\infty - \eps}^n \over 1 +x^2}\,dx  \qquad\text{by definition of }S_\eps \\
&= \qty{\norm{\phi}_\infty - \eps}^n \int_{S_\eps} { 1 \over 1 +x^2}\,dx \\
&= \qty{\norm{\phi}_\infty - \eps}^n C_\eps \qquad\text{where $C_\eps$ is some constant} \\ \\
\implies 
\qty{ \int_\RR {\abs{\phi(x)}^n \over 1 +x^2}\,dx }^{1\over n} 
&\geq \qty{\norm{\phi}_\infty - \eps} C_\eps^{1 \over n} \\
&\converges{n\to\infty}\to
\qty{\norm{\phi}_\infty - \eps} \cdot 1 \\
&\converges{\eps\to 0}\to \norm{\phi}_\infty
,\]
  where we've again used the fact that $c^{1\over n} \to 1$ for any constant.
:::
