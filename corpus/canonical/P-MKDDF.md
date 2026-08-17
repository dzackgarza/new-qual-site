---
schema: qual/card@1
id: P-MKDDF
kind: problem
title: Let $R$ be a commutative ring. Let $r \in R$. Show that the...
classification:
  areas:
  - algebra
  topics:
  - integral-domains
  - rings
  - modules
relations: []
review: draft
solved: true
---

::: problem
Let $R$ be a commutative ring.

(a) Let $r \in R$. Show that the map
    `\begin{align*}
    r\bullet : R &\to R \\
    x &\mapsto r x
    .\end{align*}`{=tex}
    is an $R\dash$module endomorphism of $R$.

(b) We say that $r$ is a **zero-divisor** if r$\bullet$ is not injective.
    Show that if $r$ is a zero-divisor and $r \neq 0$, then the kernel and image of $r\bullet$ each consist of zero-divisors.

(c) Let $n \geq 2$ be an integer. Show: if $R$ has exactly $n$ zero-divisors, then $\#R \leq n^2$ .

(d) Show that up to isomorphism there are exactly two commutative rings $R$ with precisely 2 zero-divisors.

> You may use without proof the following fact: every ring of order 4 is isomorphic to exactly one of the
> following:
> $$
> \frac{ \ZZ }{ 4\ZZ}, \quad
> \frac{ \frac{  \ZZ }{ 2\ZZ} [t]}{(t^2 + t + 1)}, \quad
> \frac{ \frac{ \ZZ }{ 2\ZZ} [t]}{ (t^2 - t)}, \quad
> \frac{ \frac{ \ZZ}{2\ZZ}[t]}{(t^2 )}
> .$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**(a) $r\bullet$ is an $R$-module endomorphism:**
For any $x, y \in R$ and $a \in R$:
1. $r\bullet(x + y) = r(x + y) = rx + ry = r\bullet(x) + r\bullet(y)$ by the distributive law.
2. $r\bullet(ax) = r(ax) = a(rx) = a \cdot r\bullet(x)$ by associativity and commutativity of multiplication in $R$.
Thus $r\bullet: R \to R$ is an $R$-linear map, i.e., an $R$-module endomorphism of $R$.

**(b) Kernel and image consist of zero-divisors:**
Let $r \neq 0$ be a zero-divisor, so $\ker(r\bullet) = \operatorname{Ann}_R(r) \neq \{0\}$.
- **Kernel:** For any $x \in \ker(r\bullet)$, $rx = 0$. Since $r \neq 0$, $r \in \ker(x\bullet)$, which means $x\bullet$ is not injective. Thus every $x \in \ker(r\bullet)$ is a zero-divisor.
- **Image:** For any $y \in \im(r\bullet)$, $y = rx$ for some $x \in R$. Since $r$ is a zero-divisor, there exists $z \neq 0$ such that $rz = 0$. Then $yz = (rx)z = (rz)x = 0 \cdot x = 0$. Since $z \neq 0$, $y\bullet(z) = 0$, so $y\bullet$ is not injective. Thus every $y \in \im(r\bullet)$ is a zero-divisor.

**(c) $\#R \leq n^2$:**
Let $Z(R)$ be the set of zero-divisors of $R$, so $|Z(R)| = n \geq 2$.
Since $n \geq 2$, there exists a non-zero zero-divisor $r \in Z(R) \setminus \{0\}$.
Consider the homomorphism $r\bullet: R \to R$.
By the First Isomorphism Theorem for $R$-modules:
$$
R / \ker(r\bullet) \cong \im(r\bullet) \implies \#R = |\ker(r\bullet)| \cdot |\im(r\bullet)|.
$$
By part (b), $\ker(r\bullet) \subseteq Z(R)$ and $\im(r\bullet) \subseteq Z(R)$.
Therefore:
$$
|\ker(r\bullet)| \leq |Z(R)| = n, \qquad |\im(r\bullet)| \leq |Z(R)| = n.
$$
Hence:
$$
\#R = |\ker(r\bullet)| \cdot |\im(r\bullet)| \leq n \cdot n = n^2.
$$

**(d) Rings with precisely 2 zero-divisors:**
Here $n = 2$, so by part (c), $\#R \leq 2^2 = 4$.
Also $0 \in Z(R)$, and since $n = 2$, there is exactly one non-zero zero-divisor, so $\#R \geq 3$.
Thus $\#R \in \{3, 4\}$.

- **If $\#R = 3$:** $R$ is a ring with 3 elements, so $(R, +) \cong \ZZ_3$. Since 3 is prime, the only unital ring of order 3 is the field $\FF_3 \cong \ZZ/3\ZZ$. But in any field, the only zero-divisor is 0, so $n = 1 \neq 2$.

- **If $\#R = 4$:** We test the 4 candidate rings of order 4 given in the problem:
  1. $R_1 = \ZZ/4\ZZ$: Elements are $\{0, 1, 2, 3\}$. The zero-divisors are $Z(R_1) = \{0, 2\}$, so $|Z(R_1)| = 2$. (Valid!)
  2. $R_2 = \FF_2[t]/(t^2 + t + 1)$: Since $t^2+t+1$ is irreducible over $\FF_2$, $R_2 \cong \FF_4$ is a field, so $|Z(R_2)| = 1 \neq 2$.
  3. $R_3 = \FF_2[t]/(t^2 - t) \cong \FF_2 \times \FF_2$: Elements are $(0,0), (1,0), (0,1), (1,1)$. Zero-divisors are $\{(0,0), (1,0), (0,1)\}$, so $|Z(R_3)| = 3 \neq 2$.
  4. $R_4 = \FF_2[t]/(t^2)$: Elements are $\{0, 1, t, 1+t\}$. Here $t \cdot t = 0$, while $(1+t)^2 = 1 + t^2 = 1 \neq 0$ (unit with inverse $1+t$). The zero-divisors are $\{0, t\}$, so $|Z(R_4)| = 2$. (Valid!)

Thus, up to isomorphism, the exactly two commutative rings with precisely 2 zero-divisors are:
$$
\ZZ/4\ZZ \quad \text{and} \quad \frac{\FF_2[t]}{(t^2)}.
$$
:::
