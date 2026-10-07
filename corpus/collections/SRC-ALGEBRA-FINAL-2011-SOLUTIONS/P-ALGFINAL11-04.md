---
schema: qual/card@1
id: P-ALGFINAL11-04
kind: problem
title: Primitive roots of unity over finite fields
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let K be a finite field of cardinality $q ,$ let $n > 0$ be an integer relatively prime to $q ,$ and let $\zeta$ be a primitive n-th root of unity lying in some field $L \supset K$ with $[ L : K ] = m$

(a) Show that n divides $q ^ { m } - 1$

[4]

(b) Show that $[ K ( \zeta ) : K ]$ is the order of $q$ in the group $( \mathbb { Z } / n \mathbb { Z } ) ^ { * }$ (units in $\mathbb { Z } / n \mathbb { Z } )$ . [6]
:::

::: {.solution}
<1>1. One has
$$
\boxed{n\mid q^m-1}.
$$
::: {.proof}
Since $[L:K]=m$ and $|K|=q$, the field $L$ has
$$
|L|=q^m
$$
elements. Hence its multiplicative group has order
$$
|L^\times|=q^m-1.
$$
Because $\zeta$ is a primitive $n$-th root of unity, it has multiplicative order exactly $n$. Lagrange's theorem gives
$$
n\mid |L^\times|=q^m-1.
$$
:::

<1>2. Put
$$
d=[K(\zeta):K].
$$
Then the multiplicative order $\mu$ of $q$ in $(\ZZ/n\ZZ)^\times$ divides $d$.
::: {.proof}
Apply step <1>1 to the finite extension $K(\zeta)/K$. Since
$$
n\mid q^d-1,
$$
one has
$$
q^d\equiv1\pmod n.
$$
By definition of the order $\mu$ of $q$ modulo $n$, this implies
$$
\mu\mid d.
$$
:::

<1>3. The field $K(\zeta)$ contains a unique subfield $K_\mu$ with
$$
[K_\mu:K]=\mu.
$$
::: {.proof}
The finite field $K(\zeta)$ has $q^d$ elements. Since $\mu\mid d$ by step <1>2, the standard subfield classification for finite fields gives a unique subfield of cardinality
$$
q^\mu,
$$
equivalently a unique subfield of degree $\mu$ over $K$.
:::

<1>4. The field $K_\mu$ contains $\zeta$.
::: {.proof}
By definition of $\mu$,
$$
q^\mu\equiv1\pmod n,
$$
so
$$
n\mid q^\mu-1=|K_\mu^\times|.
$$
The multiplicative group $K_\mu^\times$ is cyclic, hence contains a unique subgroup of order $n$.

Because $\gcd(n,q)=1$, the polynomial
$$
X^n-1
$$
has $n$ distinct roots in a splitting field. In the cyclic group $K(\zeta)^\times$, those roots form the unique subgroup of order $n$, namely
$$
\langle\zeta\rangle.
$$
The subgroup of order $n$ inside $K_\mu^\times$ must therefore be this same subgroup. Hence
$$
\zeta\in K_\mu.
$$
:::

<1>5. Therefore
$$
\boxed{[K(\zeta):K]=\mu=\operatorname{ord}_{(\ZZ/n\ZZ)^\times}(q)}.
$$
::: {.proof}
By step <1>4,
$$
K(\zeta)\subseteq K_\mu.
$$
By construction in step <1>3,
$$
K_\mu\subseteq K(\zeta).
$$
Thus the two fields are equal, and their degree over $K$ is $\mu$.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>1 proves part (a), and step <1>5 proves part (b).
:::
:::
