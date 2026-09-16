---
schema: qual/card@1
id: P-HCAO2
kind: problem
title: The unit group of $\mathbb Z/(q-1)\mathbb Z$
classification:
  areas:
  - algebra
  topics:
  - Modular Arithmetic
  - Unit Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the question with the retained Harvard commutative-algebra extraction, which gives no additional condition on q; the answer treats every integer q."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the Bezout unit criterion, all Chinese-remainder factors, the odd-prime lifting argument, the powers of five for powers of two, and both exceptional moduli."
---

::: {.problem}
Let $q$ be an integer.
What is $\left(\mathbb Z/(q-1)\mathbb Z\right)^\times$?
:::

::: {.solution}
Put $N=|q-1|$. Write $C_d$ for a cyclic group of order $d$,
with $C_1$ the trivial group. For $N\geq2$, factor
$N=\prod_{\ell\mid N}\ell^{e_\ell}$ into prime powers.
Then the complete group description is
$$
(\mathbb Z/N\mathbb Z)^\times
\cong\prod_{\ell\mid N}U(\ell,e_\ell),
$$
where
$$
\begin{aligned}
U(\ell,e)&=C_{\ell^{e-1}(\ell-1)} &&(\ell\text{ odd}),\\
U(2,1)&=C_1,\qquad U(2,2)=C_2,\\
U(2,e)&=C_2\times C_{2^{e-2}} &&(e\geq3).
\end{aligned}
$$
The elements are precisely the residue classes $\bar a$
with $\gcd(a,N)=1$, under multiplication, and their number is
$\varphi(N)=N\prod_{\ell\mid N}(1-1/\ell)$.
For $N=0$ the ring is $\mathbb Z$ and its unit group is
$\{1,-1\}\cong C_2$. For $N=1$ the ring has one element
and its unit group is trivial.

<1>1. The coprimality criterion and product decomposition hold.

::: {.proof}
For $N\geq2$, a residue class $\bar a$ is a unit exactly
when $ab\equiv1\pmod N$ for some integer $b$.
Such an equality gives $ab+cN=1$, implying $\gcd(a,N)=1$.
Conversely Bezout's identity supplies such $b,c$ when the
gcd is one [@DF04]. The Chinese remainder ring isomorphism
$$
\mathbb Z/N\mathbb Z\longrightarrow
\prod_{\ell\mid N}\mathbb Z/\ell^{e_\ell}\mathbb Z
$$
therefore restricts to an isomorphism of unit groups:
a tuple in a product ring is invertible exactly when
every coordinate is invertible [@DF04].
Modulo $\ell^e$, exactly $\ell^{e-1}$ residues are divisible
by $\ell$, and all other residues are units. Thus that
factor has $\ell^{e-1}(\ell-1)$ units. Multiplying the
factor sizes proves the asserted formula for $\varphi(N)$.
:::

<1>2. For an odd prime $\ell$, the units modulo $\ell^e$
form a cyclic group of order $\ell^{e-1}(\ell-1)$.

::: {.proof}
The multiplicative group of the finite field $\mathbb F_\ell$
is cyclic [@DF04]. Choose an integer $a$ whose residue has
order $\ell-1$. There is a choice $b=a$ or $b=a+\ell$
such that
$$
b^{\ell-1}=1+\ell c,\qquad \ell\nmid c.
$$
Indeed, $a^{\ell-1}\equiv1\pmod\ell$. If it is not
one modulo $\ell^2$, use $b=a$. Otherwise binomial expansion gives
$$
(a+\ell)^{\ell-1}
\equiv a^{\ell-1}+\ell(\ell-1)a^{\ell-2}
\not\equiv1\pmod{\ell^2},
$$
since $\ell$ divides neither $a$ nor $\ell-1$.
Both choices still have order $\ell-1$ modulo $\ell$.

For an integer $u\geq1$ and $\ell\nmid d$, expansion shows
$$
(1+\ell^u d)^\ell
\equiv1+\ell^{u+1}d\pmod{\ell^{u+2}}.
$$
For terms with exponent $2\leq j<\ell$, the binomial
coefficient contributes a factor $\ell$, and $uj+1\geq u+2$.
The last term has exponent $u\ell\geq u+2$ because
$\ell\geq3$. Thus the displayed first nonzero term cannot
cancel. By induction, for every $j\geq0$ the integer
$b^{(\ell-1)\ell^j}-1$ is divisible by $\ell^{j+1}$
but not by $\ell^{j+2}$.

Let $d_e$ be the order of $b$ modulo $\ell^e$.
Reduction modulo $\ell$ makes $\ell-1$ divide $d_e$,
and Lagrange's theorem and step <1>1 make $d_e$ divide
$(\ell-1)\ell^{e-1}$. Hence $d_e=(\ell-1)\ell^h$
for $0\leq h\leq e-1$. The preceding exact divisibility
forces $h+1\geq e$. Thus $h=e-1$, giving an element
whose order equals the whole unit-group order, as required.
:::

<1>3. The factors at powers of two have the stated structure.

::: {.proof}
Modulo $2$ there is one unit. Modulo $4$ the units are
$1,-1$, giving $C_2$. Now let $e\geq3$.
For every $j\geq0$, the integer $5^{2^j}-1$ is divisible
by $2^{j+2}$ but not by $2^{j+3}$. The base case is
$5-1=4$. For the induction step, factor
$$
5^{2^{j+1}}-1=(5^{2^j}-1)(5^{2^j}+1).
$$
The second factor is congruent to $2$ modulo $4$, while
the first has the asserted exact power of two.
It follows that the residue of $5$ modulo $2^e$ has
order $2^{e-2}$. Here its order is a power of two by
Lagrange's theorem, and the exact divisibilities identify
the smallest power that gives one.

Every power of $5$ is one modulo $4$. There are precisely
$2^{e-2}$ residues with that property modulo $2^e$,
so these residues are exactly $\langle5\rangle$.
Every odd residue is either one or minus one modulo $4$;
therefore every unit is uniquely $(-1)^\varepsilon5^j$,
with $\varepsilon\in\{0,1\}$ and $j$ modulo $2^{e-2}$.
Uniqueness follows because $-1$ is three modulo $4$
and is not in $\langle5\rangle$. The factors commute,
so this gives $C_2\times C_{2^{e-2}}$.
:::

<1>4. The exceptional moduli cause no additional cases.

::: {.proof}
The ideals $(q-1)$ and $(|q-1|)$ in $\mathbb Z$ coincide.
When $q=1$, the quotient by $(0)$ is $\mathbb Z$;
its only integer units are $1,-1$. When $|q-1|=1$,
the quotient is the zero ring. Its sole element is its
identity and is its own multiplicative inverse, so its
unit group has one element. All other integers $q$
give $N\geq2$ and are covered by steps <1>1–<1>3.
:::
:::
