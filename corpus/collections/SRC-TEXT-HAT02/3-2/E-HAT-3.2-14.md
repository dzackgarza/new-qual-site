---
schema: qual/card@1
id: E-HAT-3.2-14
kind: problem
title: Surjection from $\CP^\infty$ to $\RP^\infty$ on cohomology
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $q: \RP^\infty \to \CP^\infty$ be the natural quotient map obtained by regarding both spaces as quotients of $S^\infty$, modulo multiplication by real scalars in one case and complex scalars in the other.
Show that the induced map $q^*: H^*(\CP^\infty; \ZZ) \to H^*(\RP^\infty; \ZZ)$ is surjective in even dimensions by showing first by a geometric argument that the restriction $q: \RP^2 \to \CP^1$ induces a surjection on $H^2$ and then appealing to cup product structures.

Next, form a quotient space $X$ of $\RP^\infty \amalg \CP^n$ by identifying each point $x \in \RP^{2n}$ with $q(x) \in \CP^n$.
Show there are ring isomorphisms $H^*(X; \ZZ) \approx \ZZ[\alpha]/(2\alpha^{n+1})$ and $H^*(X; \ZZ_2) \approx \ZZ_2[\alpha, \beta]/(\beta^2 - \alpha^{2n+1})$, where $\gradeddegree{\alpha} = 2$ and $\gradeddegree{\beta} = 2n+1$.
Make a similar construction and analysis for the quotient map $q: \CP^\infty \to \quatprojective^\infty$.
:::

::: {.solution}
Write $\RR^{2k+1} = \CC^k \oplus \RR \subset \CC^{k+1}$, so that $\RP^{2k} \subset \RP^\infty$ maps into $\CP^k$ under $q$ and $\RP^{2k-1} = S(\CC^k)/\pm 1$ maps into $\CP^{k-1}$.
Likewise write $\CC^{2k+1} = \HH^k \oplus \CC \subset \HH^{k+1}$ for the quaternionic quotient $q \colon \CP^\infty \to \quatprojective^\infty$, which maps $\CP^{2k}$ into $\quatprojective^k$ and $\CP^{2k-1}$ into $\quatprojective^{k-1}$.
Projective spaces carry their standard CW structures with one cell in each dimension $0, 1, 2, \dots$ (real), $0, 2, 4, \dots$ (complex), $0, 4, 8, \dots$ (quaternionic).
Let $x \in H^2(\CP^\infty;\ZZ)$ and $u \in H^4(\quatprojective^\infty;\ZZ)$ be the polynomial generators, $w \in H^1(\RP^\infty;\ZZ_2)$ the polynomial generator over $\ZZ_2$, and $\gamma$ the generator of $H^2(\RP^\infty;\ZZ) \cong \ZZ_2$.

::: pf

::: {.pf-step #top-cell}
For each $k \ge 1$, $q$ maps $\RP^{2k} \setminus \RP^{2k-1}$ homeomorphically onto $\CP^k \setminus \CP^{k-1}$, and so induces a homeomorphism $\RP^{2k}/\RP^{2k-1} \to \CP^k/\CP^{k-1}$; likewise $q$ induces a homeomorphism $\CP^{2k}/\CP^{2k-1} \to \quatprojective^k/\quatprojective^{k-1}$.

::: pf-proof
A point of $\RP^{2k} \setminus \RP^{2k-1}$ is $\pm(v, t)$ with $v \in \CC^k$, $t \in \RR \setminus 0$, $\norm{v}^2 + t^2 = 1$; it has a unique representative with $t > 0$, so these points correspond bijectively to the open disk $\{\norm{v} < 1\}$.
A point of $\CP^k \setminus \CP^{k-1}$ is a complex line spanned by $(v, s)$ with $s \in \CC \setminus 0$; multiplying by a unit complex scalar gives a unique representative with $s > 0$ real and $\norm{v}^2 + s^2 = 1$, again a point of the open disk $\{\norm{v} < 1\}$.
In these coordinates $q$ is the identity of the disk.
Hence the induced map $\RP^{2k}/\RP^{2k-1} \to \CP^k/\CP^{k-1}$ is a continuous bijection from a compact space to a Hausdorff space, hence a homeomorphism.
The quaternionic case is the same argument with $(v, z) \in \HH^k \oplus \CC$, normalising $z$ by a unit complex scalar and $s \in \HH$ by a unit quaternion to a positive real.
:::

:::

::: {.pf-step #part1}
$q^* \colon H^{2k}(\CP^\infty;\ZZ) \to H^{2k}(\RP^\infty;\ZZ)$ is surjective for every $k$.

::: pf-proof

::: {.pf-step #h2}
The restriction $q \colon \RP^2 \to \CP^1$ induces a surjection on $H^2(-;\ZZ)$, and $q^* x = \gamma$.

::: pf-proof
By step [](#top-cell){.pf-ref} with $k = 1$, $q \colon \RP^2 \to \CP^1 = S^2$ is the quotient map collapsing $\RP^1$ to the point $\CP^0$.
So $q^*$ on $H^2$ is the map $H^2(\RP^2, \RP^1) \to H^2(\RP^2)$ of the long exact sequence of the pair, which is surjective since $H^2(\RP^1) = 0$.
Restriction to the $2$-skeleton is injective on $H^2$ for any CW complex; since $H^2(\RP^\infty;\ZZ) \cong \ZZ_2 \cong H^2(\RP^2;\ZZ)$ and $H^2(\CP^\infty;\ZZ) \cong \ZZ \cong H^2(\CP^1;\ZZ)$, both restrictions are isomorphisms on $H^2$.
They commute with $q$, so $q^* x$ generates $H^2(\RP^\infty;\ZZ)$, that is, $q^* x = \gamma$.
:::

:::

::: {.pf-step #rp-ring}
$\gamma^k$ generates $H^{2k}(\RP^\infty;\ZZ) \cong \ZZ_2$ for $k \ge 1$.

::: pf-proof
The cellular boundary in $\RP^\infty$ is $d e^m = (1 + (-1)^m) e^{m-1}$, so $H^{2k}(\RP^\infty;\ZZ) \cong \ZZ_2$ for $k \ge 1$.
Reduction mod $2$, $\rho \colon H^{2k}(\RP^\infty;\ZZ) \to H^{2k}(\RP^\infty;\ZZ_2)$, is injective: its kernel is the image of multiplication by $2$, which is zero on $\ZZ_2$.
Both groups are $\ZZ_2$, so $\rho$ is an isomorphism; it is a ring map, so $\rho(\gamma) = w^2$ and $\rho(\gamma^k) = w^{2k} \neq 0$.
:::

:::

::: pf-step
$q^*$ is surjective in even degrees.

::: pf-proof
$q^*$ is a ring homomorphism, so $q^*(x^k) = \gamma^k$ by step [](#h2){.pf-ref}, and $\gamma^k$ generates $H^{2k}(\RP^\infty;\ZZ)$ by step [](#rp-ring){.pf-ref}; in degree $0$, $q^*$ is the identity of $\ZZ$.
:::

:::

:::

:::

::: {.pf-step #x-cells}
$X$ is a CW complex whose cells are those of $\CP^n$ together with the cells $e^m$, $m \ge 2n+1$, of $\RP^\infty$; the quotient map $j \colon \RP^\infty \to X$ and the inclusion $i \colon \CP^n \to X$ are cellular; and the cellular boundary of $X$ vanishes except $d e^m = 2 e^{m-1}$ for even $m \ge 2n+2$.

::: pf-proof
$X$ is obtained from $\CP^n$ by attaching the cells of $\RP^\infty$ of dimension at least $2n+1$, each attaching map being the attaching map in $\RP^\infty$ followed by $q$ on $\RP^{2n}$.
The cells of $\CP^n$ are in even dimensions only, so their boundaries vanish.
For $m \ge 2n+2$, $X^{m-1}/X^{m-2} = \RP^{m-1}/\RP^{m-2}$ and the boundary coefficient is that of $\RP^\infty$, namely $1 + (-1)^m$.
For $e^{2n+1}$, the coefficient on $e^{2n}$ is the degree of $S^{2n} \to \RP^{2n} \to \RP^{2n}/\RP^{2n-1} \to \CP^n/\CP^{n-1}$; the last map is a homeomorphism by step [](#top-cell){.pf-ref}, and the first composite has degree $1 + (-1)^{2n+1} = 0$.
:::

:::

::: {.pf-step #x-detect}
For any coefficients, $i^*$ is an isomorphism on $H^m(X)$ for $m \le 2n$ and $j^*$ is an isomorphism on $H^m(X)$ for $m \ge 2n+2$; with $\ZZ_2$ coefficients $j^*$ is also an isomorphism for $m = 2n+1$.

::: pf-proof
By step [](#x-cells){.pf-ref}, $i$ identifies the cellular cochain complex of $\CP^n$ with that of $X$ in degrees at most $2n$, and the coboundary $C^{2n} \to C^{2n+1}$ of $X$ is zero.
Likewise $j$ identifies the cochain complexes in degrees at least $2n+1$, and $H^m$ for $m \ge 2n+2$ depends only on degrees $m-1, m, m+1$.
With $\ZZ_2$ coefficients all coboundaries of $X$ and $\RP^\infty$ vanish, so $H^m = C^m$ and $j^*$ is an isomorphism in degree $2n+1$ too.
:::

:::

::: pf-step
$H^*(X;\ZZ) \cong \boxed{\ZZ[\alpha]/(2\alpha^{n+1})}$ with $\gradeddegree{\alpha} = 2$.

::: pf-proof
The map $p \colon X \to \CP^\infty$ equal to $q$ on $\RP^\infty$ and to the inclusion on $\CP^n$ is well defined; let $\alpha = p^* x$.
Then $i^* \alpha$ generates $H^2(\CP^n)$ and $j^* \alpha = q^* x = \gamma$ by step [](#h2){.pf-ref}.
By step [](#x-cells){.pf-ref}, $H^m(X;\ZZ)$ is $\ZZ$ for $m = 0, 2, \dots, 2n$, is $\ZZ_2$ for even $m \ge 2n+2$, and is $0$ for odd $m$ (in degree $2n+1$ because $\delta(e^{2n+1})^* = 2(e^{2n+2})^*$ is injective).
By step [](#x-detect){.pf-ref}, $\alpha^k$ generates $H^{2k}(X;\ZZ)$: for $k \le n$ because $i^* \alpha^k$ generates $H^{2k}(\CP^n)$, and for $k \ge n+1$ because $j^* \alpha^k = \gamma^k$ generates $H^{2k}(\RP^\infty;\ZZ)$ by step [](#rp-ring){.pf-ref}.
So $\ZZ[\alpha] \to H^*(X;\ZZ)$ is surjective, with kernel $0$ in degrees $2k \le 2n$ and $2\ZZ\alpha^k$ in degrees $2k \ge 2n+2$, which is the ideal $(2\alpha^{n+1})$.
:::

:::

::: pf-step
$H^*(X;\ZZ_2) \cong \boxed{\ZZ_2[\alpha, \beta]/(\beta^2 - \alpha^{2n+1})}$ with $\gradeddegree{\alpha} = 2$, $\gradeddegree{\beta} = 2n+1$.

::: pf-proof
By step [](#x-cells){.pf-ref} all coboundaries vanish mod $2$, so $H^m(X;\ZZ_2) \cong \ZZ_2$ for $m \in \{0, 2, \dots, 2n\}$ and every $m \ge 2n+1$, and is $0$ otherwise.
Let $\alpha$ now denote the reduction of $p^* x$, and let $\beta$ be the generator of $H^{2n+1}(X;\ZZ_2)$, so $j^* \alpha = w^2$ by step [](#rp-ring){.pf-ref} and $j^* \beta = w^{2n+1}$ by step [](#x-detect){.pf-ref}.
Then $\alpha^k$ generates $H^{2k}(X;\ZZ_2)$ for $k \le n$ (via $i^*$) and for $k \ge n+1$ (via $j^* \alpha^k = w^{2k}$), and $\beta \alpha^l$ generates $H^{2n+1+2l}(X;\ZZ_2)$ because $j^*(\beta\alpha^l) = w^{2n+1+2l}$.
Since $j^*(\beta^2) = w^{4n+2} = j^*(\alpha^{2n+1})$ and $j^*$ is injective in degree $4n+2$, $\beta^2 = \alpha^{2n+1}$.
So $\ZZ_2[\alpha,\beta]/(\beta^2 - \alpha^{2n+1}) \to H^*(X;\ZZ_2)$ is a surjective ring map.
The source has $\ZZ_2$-basis $\{\alpha^k, \beta\alpha^l : k, l \ge 0\}$, one element in each degree $0, 2, \dots, 2n$ and in each degree at least $2n+1$, matching the target, so the map is an isomorphism.
:::

:::

::: pf-step
For $q \colon \CP^\infty \to \quatprojective^\infty$: $q^* u = x^2$ for a suitable choice of sign of $u$, so $q^*$ maps $H^*(\quatprojective^\infty;\ZZ) = \ZZ[u]$ isomorphically onto the subring $\ZZ[x^2]$, and is surjective exactly in degrees divisible by $4$.

::: pf-proof
By step [](#top-cell){.pf-ref} with $k = 1$, $q \colon \CP^2 \to \quatprojective^1 = S^4$ collapses $\CP^1$ to a point, so on $H^4$ it is the map $H^4(\CP^2, \CP^1) \to H^4(\CP^2)$, an isomorphism since $H^3(\CP^1) = H^4(\CP^1) = 0$.
The restrictions $H^4(\quatprojective^\infty) \to H^4(\quatprojective^1)$ and $H^4(\CP^\infty) \to H^4(\CP^2)$ are isomorphisms (restriction to the $5$-skeleton), so $q^* u = \pm x^2$, and $q^*(u^k) = x^{2k}$ after fixing the sign of $u$.
The groups $H^{4k+2}(\CP^\infty) = \ZZ x^{2k+1}$ are not hit, as $H^{4k+2}(\quatprojective^\infty) = 0$.
:::

:::

::: pf-step
Let $Y$ be the quotient of $\CP^\infty \amalg \quatprojective^n$ identifying each $y \in \CP^{2n}$ with $q(y) \in \quatprojective^n$.
Then $H^*(Y;\ZZ) \cong \boxed{\ZZ[\mu, \nu]/(\nu^2 - \mu^{2n+1})}$ with $\gradeddegree{\mu} = 4$, $\gradeddegree{\nu} = 4n+2$, and $H^*(Y;\ZZ_2) \cong \ZZ_2[\mu,\nu]/(\nu^2 - \mu^{2n+1})$.

::: pf-proof
As in step [](#x-cells){.pf-ref}, $Y$ is $\quatprojective^n$ with the cells of $\CP^\infty$ of dimension at least $4n+2$ attached; all cells have even dimension, so all cellular coboundaries vanish and $H^m(Y;R) \cong R$ for $m \in \{0, 4, \dots, 4n\}$ and every even $m \ge 4n+2$, and $0$ otherwise, for $R = \ZZ$ or $\ZZ_2$.
As in step [](#x-detect){.pf-ref}, the inclusion $i \colon \quatprojective^n \to Y$ induces isomorphisms in degrees at most $4n$ and the quotient map $j \colon \CP^\infty \to Y$ induces isomorphisms in degrees at least $4n+2$.
Let $\mu$ be the pullback of $u$ under the map $Y \to \quatprojective^\infty$ equal to $q$ on $\CP^\infty$ and the inclusion on $\quatprojective^n$, and let $\nu$ generate $H^{4n+2}(Y;R)$ with $j^* \nu = x^{2n+1}$.
Then $j^* \mu = x^2$, so $\mu^k$ generates $H^{4k}(Y;R)$ for all $k$ (via $i^*$ for $k \le n$, via $j^* \mu^k = x^{2k}$ for $k \ge n+1$), and $\nu\mu^l$ generates $H^{4n+2+4l}(Y;R)$ because $j^*(\nu\mu^l) = x^{2n+1+2l}$.
Since $j^*(\nu^2) = x^{4n+2} = j^*(\mu^{2n+1})$, $\nu^2 = \mu^{2n+1}$.
The ring $R[\mu,\nu]/(\nu^2 - \mu^{2n+1})$ is free over $R$ on $\{\mu^k, \nu\mu^l\}$, one generator in each degree where $H^*(Y;R) \cong R$, so the surjection onto $H^*(Y;R)$ is an isomorphism.
:::

:::

:::

:::
