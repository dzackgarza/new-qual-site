---
schema: qual/card@1
id: P-CAF08B
kind: problem
title: "True or False: meromorphic extensions, Schwarz reflection, simple connectivity, minimum modulus, and analytic continuation"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
For each part, determine if it is always true or sometimes false.
If true give a brief proof.
If false give a counterexample.

(a) If $f \in H(B(1; 1) \setminus \{1\})$ with $|f(z)| \leq \frac{1}{|z - 1|}$ for all $z \in B(1; 1) \setminus \{1\}$, then $f$ extends to a meromorphic (or possibly analytic) function on $B(1; 1)$.

(b) Suppose that $f \in H(\{z \in B(0; 1) : \operatorname{Re} z > 0\})$ and extends continuously to the line segment $I = \{it : -1 < t < 1\}$.
If $f(I) \subset i\mathbb{R}$, then $f$ extends to an analytic function in $B(0; 1)$.

(c) If $G \subset \mathbb{C}$ is open, connected, and simply connected, and $f \in H(G)$ with $f'(z) \neq 0$ for all $z \in G$, then $f(G)$ is also open, connected, and simply connected.

(d) Let $G \subset \mathbb{C}$ be connected and open and $f \in H(G)$ nonconstant.
If $f(z) \neq 0$ for all $z \in G$, then $|f|$ does not reach a minimum at any point in $G$.

(e) Let $f$ be an analytic function element defined in $B(1/2; 1/4)$.
Suppose that $f$ continues analytically along any path $\gamma$ from $\gamma(0) \in B(1/2; 1/4)$ to $\gamma(1) \in B(0; 1) \setminus \{0\}$.
Then there is a function $F \in H(B(0; 1) \setminus \{0\})$ such that $F|_{B(1/2; 1/4)} = f$.
:::

::: solution
<1>1. (a) **True.** Put $g(z)=(z-1)f(z)$. Then $|g(z)|\le1$ on the punctured disk, so $g$ has a removable singularity at $1$. Hence $f(z)=\widetilde g(z)/(z-1)$ has at worst a simple pole at $1$ and extends meromorphically.

<1>2. (b) **True.** On the left half-disk define
$$
F(z)=-\overline{f(-\bar z)}.
$$
For $z=it\in I$, one has $-\bar z=z$, and $f(it)\in i\mathbb R$ implies $-\overline{f(it)}=f(it)$. Thus the reflected function matches continuously across $I$. Schwarz reflection, equivalently Morera's theorem across the diameter, yields a holomorphic extension to $B(0;1)$.

<1>3. (c) **False.** Take $G=\mathbb C$ and $f(z)=e^z$. Then $f'(z)\ne0$ everywhere, but $f(G)=\mathbb C^*$ is not simply connected.

<1>4. (d) **True.** Since $f$ has no zero, $1/f$ is holomorphic. An interior minimum of $|f|$ would give an interior maximum of $|1/f|$, forcing $f$ to be constant by the maximum-modulus principle.

<1>5. (e) **False.** Take a branch of $\log z$ on $B(1/2;1/4)$. It analytically continues along every path in $B(0;1)\setminus\{0\}$, but continuation once around $0$ changes its value by $2\pi i$. Hence there is no single-valued holomorphic extension to the punctured disk.
:::
