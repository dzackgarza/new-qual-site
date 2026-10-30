---
schema: qual/card@1
id: P-TATE85-X7-02
kind: problem
title: Galois group of $X^7-7X+3$
classification:
  areas:
  - algebra
  topics:
  - Galois Groups of Polynomials
  - Chebotarev Density Theorem
  - Simple Groups
relations: []
review: draft
---

::: {.problem}
(II) Let $f(X) = X^{7} - 7X + 3$ (shown me by Mr. Elkies). It is easy to check that $f(X)$ satisfies the conditions of (I). For example, $d_{f} = 3^{8} \cdot 7^{8}$. Moreover, out of the first $360$ primes:
$$
p = 2, 3, 5, 7, \ldots, 2423:
$$

- $f(X)$ has no root $\pmod{p}$ for $104$ $p$'s;
- $f(X)$ has $1$ root $\pmod{p}$ for $214$ $p$'s;
- $f(X)$ has $3$ roots $\pmod{p}$ for $41$ $p$'s;
- $f(X)$ has $7$ roots $\pmod{p}$ for $1$ $p$ (namely $p = 1879$);

Is $G_{f} = G_{168}$, or $A_{7}$?
:::

::: {.solution}

Let $L$ be the splitting field of
$$
f(X)=X^7-7X+3
$$
over $\QQ$, and put $G=\operatorname{Gal}(L/\QQ)$.

::: pf

::: {.pf-step #s1-1}

The polynomial $f$ is irreducible over $\QQ$.


::: pf-proof

Modulo $2$,
$$
f(X)\equiv X^7+X+1.
$$
This polynomial has no root in $\FF_2$. The only monic irreducible quadratic over $\FF_2$ is
$$
X^2+X+1,
$$
and the two monic irreducible cubics are
$$
X^3+X+1,
\qquad
X^3+X^2+1.
$$
Division of $X^7+X+1$ by these three polynomials leaves remainders $1$, $X$, and $X$, respectively. Hence it has no irreducible factor of degree $1$, $2$, or $3$. A reducible polynomial of degree $7$ must have a factor of degree at most $3$, so $X^7+X+1$ is irreducible over $\FF_2$. Gauss's lemma therefore gives the irreducibility of $f$ over $\QQ$.

:::

:::

::: {.pf-step #s1-2}

By part (I),
$$
G\cong A_7
\qquad\text{or}\qquad
G\cong G_{168}.
$$


::: pf-proof

The discriminant is
$$
\operatorname{disc}(f)=3^8 7^8=(3^4 7^4)^2,
$$
and the source states that $f$ has exactly three real roots. Together with the irreducibility from step [](#s1-1){.pf-ref}, these are precisely the hypotheses of part (I), whose conclusion is the displayed dichotomy.

:::

:::

::: {.pf-step #s1-3}

Let $\alpha_1,\ldots,\alpha_7$ be the roots of $f$ and form the three-set resolvent
$$
P_{35}(T)
=
\prod_{1\le i<j<k\le7}
\bigl(T-(\alpha_i+\alpha_j+\alpha_k)\bigr)
\in\QQ[T].
$$
For this polynomial, exact symmetric expansion gives
$$
\begin{aligned}
P_{35}(T)={}&T^{35}-280T^{29}+906T^{28}-79086T^{23}-56826T^{22}
+34452T^{21}\\
&+1739696T^{17}+408366T^{16}+1139292T^{15}+978750T^{14}\\
&-12357947T^{11}+1393266T^{10}-9345672T^9+4975614T^8
-592029T^7\\
&+29042496T^5-12446784T^4-2222640T^3+1227744T^2
+36288T-31104.
\end{aligned}
$$
Moreover,
$$
P_{35}(T)
=
\bigl(T^7+14T^4-42T^2-21T+9\bigr)R_{28}(T),
$$
for some $R_{28}(T)\in\ZZ[T]$ of degree $28$, and
$$
\gcd(P_{35},P_{35}')=1.
$$


::: pf-proof

The coefficients of $P_{35}$ are symmetric polynomials in the roots of $f$, hence are polynomials in the elementary symmetric functions of those roots. For
$$
f(X)=X^7-7X+3,
$$
these elementary symmetric functions vanish except for the coefficients corresponding to $X$ and the constant term. Newton identities therefore give the displayed polynomial.

Ordinary polynomial division of that explicit polynomial by
$$
T^7+14T^4-42T^2-21T+9
$$
has remainder $0$, proving the displayed factorization. The Euclidean algorithm applied to the same explicit polynomial and its derivative gives gcd $1$. Hence $P_{35}$ is reducible and has $35$ distinct roots.

:::

:::

::: {.pf-step #s1-4}

The alternative $G\cong A_7$ is impossible.


::: pf-proof

The group $A_7$ acts transitively on the $35$ three-element subsets of $\{1,\ldots,7\}$. By step [](#s1-3){.pf-ref} the corresponding $35$ three-root sums are all distinct. Therefore, if $G=A_7$, the Galois conjugates of any root
$$
\alpha_i+\alpha_j+\alpha_k
$$
of the three-set resolvent run through all $35$ roots of $P_{35}$. Consequently $P_{35}$ is irreducible over $\QQ$.

Step [](#s1-3){.pf-ref} shows instead that $P_{35}$ has factors of degrees $7$ and $28$. Hence $G\ne A_7$.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{G_f\cong G_{168}\cong \operatorname{GL}_3(\FF_2)
\cong \operatorname{PSL}_2(\FF_7)}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} leaves only $A_7$ and $G_{168}$, and step [](#s1-4){.pf-ref} excludes $A_7$.

:::

:::

::: pf-step

The supplied prime counts are consistent with this exact conclusion.


::: pf-proof

In the natural action of $G_{168}=\operatorname{GL}_3(\FF_2)$ on the seven nonzero vectors of $\FF_2^3$, the numbers of fixed points of an element can only be $0$, $1$, $3$, or $7$. For an unramified prime, the number of roots of $f$ modulo $p$ is the number of fixed points of a Frobenius element. Thus the observed root counts $0$, $1$, $3$, and $7$ have exactly the pattern expected for $G_{168}$.

The finite table is corroborating evidence rather than the logical step that excludes $A_7$; that exclusion is supplied by the exact resolvent factorization in steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested Galois group.

:::

:::

:::
