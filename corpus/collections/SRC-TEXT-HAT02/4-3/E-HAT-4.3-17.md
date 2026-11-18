---
schema: qual/card@1
id: E-HAT-4.3-17
kind: problem
title: "$\\Omega X$ is an H-space"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 17; corrected the stored subject from X to ΩX.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps. The route is that of Sam, Solutions to Algebraic
    Topology (2008), Section 4.3 Exercise 17 (retained text, tmp/sources/hatcher-solutions-sam-2008.md),
    whose answer is that concatenation is associative up to homotopy and that the constant loop is a
    unit up to homotopy. Supplied here what the prose left to the reader: the explicit based
    homotopies showing the constant loop is a two-sided unit, which is the condition Hatcher's
    definition on printed p. 281 actually requires (the unit homotopies must be through based maps),
    the pasting argument for continuity of concatenation, the two-breakpoint family giving
    associativity up to homotopy, and the reversal formula. Also noted that associativity and
    inverses are not part of the H-space definition, so they are recorded as extra structure rather
    than as needed hypotheses.

---

::: {.problem}
Show that $\Omega X$ is an H-space with multiplication the composition of loops.
:::

::: {.solution}

The route is that of Sam, *Solutions to Algebraic Topology* (2008), §4.3 Exercise 17 (`tmp/sources/hatcher-solutions-sam-2008.md`): concatenation of loops is a multiplication which is associative up to homotopy and has the constant loop as a unit up to homotopy. The explicit homotopies and the pasting argument are written out below.

Let $X$ be a space with basepoint $x_{0}$ and let $\Omega X$ be the space of based loops $\alpha\colon I\to X$, $\alpha(0)=\alpha(1)=x_{0}$, with the compact-open topology. Let $e$ denote the constant loop at $x_{0}$.

::: pf

::: {.pf-step #concat}
The formula
$$
(\alpha*\beta)(t)=\begin{cases}\alpha(2t),&0\leq t\leq\tfrac12,\\[2pt] \beta(2t-1),&\tfrac12\leq t\leq1\end{cases}
$$
defines a continuous map $\mu\colon\Omega X\times\Omega X\to\Omega X$.

::: pf-proof
For fixed $\alpha,\beta$ the two formulas agree at $t=\tfrac12$, where both give $\alpha(1)=x_{0}=\beta(0)$, and each is continuous on its closed half of $I$, so by the pasting lemma $\alpha*\beta$ is a continuous path; it is based at $x_{0}$ because $(\alpha*\beta)(0)=\alpha(0)=x_{0}$ and $(\alpha*\beta)(1)=\beta(1)=x_{0}$. Continuity in $(\alpha,\beta,t)$ jointly follows because the evaluation map $(\alpha,t)\mapsto\alpha(t)$ is continuous and the given reparametrizations of $t$ are continuous; hence $\mu$ is continuous.
:::

:::

::: {.pf-step #right-unit}
$\alpha*e$ is homotopic to $\alpha$ through based loops, for every $\alpha$.

::: pf-proof
Define $H\colon I\times I\to X$ by $H(t,s)=\alpha\bigl(\min(1,\,2t/(2-s))\bigr)$ for $0\leq s\leq1$. The argument of $\alpha$ is continuous in $(t,s)$ and lies in $[0,1]$; at $s=0$ it is $t$, giving $H(\cdot,0)=\alpha$; at $s=1$ it is $\min(1,2t)$, which equals $2t$ for $t\leq\tfrac12$ and $1$ for $t\geq\tfrac12$, giving $H(\cdot,1)=\alpha*e$ because the second half of $\alpha*e$ is the constant $x_{0}=\alpha(1)$. For every $s$, $H(0,s)=\alpha(0)=x_{0}$ and $H(1,s)=\alpha(1)=x_{0}$, so the homotopy is through based loops.
:::

:::

::: {.pf-step #left-unit}
$e*\alpha$ is homotopic to $\alpha$ through based loops.

::: pf-proof
Define $H(t,s)=\alpha\bigl(\max(0,\,(2t-s)/(2-s))\bigr)$. At $s=0$ the argument is $\max(0,t)=t$; at $s=1$ it is $\max(0,2t-1)$, which is $0$ for $t\leq\tfrac12$ and $2t-1$ for $t\geq\tfrac12$, matching $e*\alpha$ since its first half is the constant $x_{0}=\alpha(0)$. Continuity holds because at $2t=s$ both expressions give $\alpha(0)=x_{0}$, and the homotopy is based at every stage.
:::

:::

::: {.pf-step #hspace}
$(\Omega X,\mu,e)$ is an H-space.

::: pf-proof
By Hatcher's definition (printed p. 281) an H-space is a space with basepoint $e$ and a continuous multiplication $\mu$ such that $x\mapsto\mu(x,e)$ and $x\mapsto\mu(e,x)$ are homotopic to the identity through maps $(X,e)\to(X,e)$. Here $\mu$ is continuous by step [](#concat){.pf-ref}, and steps [](#right-unit){.pf-ref} and [](#left-unit){.pf-ref} give the two based homotopies from $\mu(-,e)$ and $\mu(e,-)$ to the identity of $\Omega X$.
:::

:::

::: {.pf-step #assoc}
$\mu$ is associative up to homotopy: $(\alpha*\beta)*\gamma\simeq\alpha*(\beta*\gamma)$ through based loops.

::: pf-proof
$(\alpha*\beta)*\gamma$ runs through $\alpha$ on $[0,\tfrac14]$, $\beta$ on $[\tfrac14,\tfrac12]$ and $\gamma$ on $[\tfrac12,1]$, while $\alpha*(\beta*\gamma)$ uses the breakpoints $\tfrac12,\tfrac34$. For $s\in[0,1]$ let $a(s)=\tfrac{1+s}{4}$ and $b(s)=\tfrac{1+s}{2}$, so $a(0)=\tfrac14$, $b(0)=\tfrac12$ and $a(1)=\tfrac12$, $b(1)=\tfrac34$, and let $L_{s}$ be the based loop which is $\alpha$ on $[0,a(s)]$, $\beta$ on $[a(s),b(s)]$ and $\gamma$ on $[b(s),1]$, each linearly reparametrized. The formula is continuous in $(t,s)$ and its value at the breakpoints is $x_{0}$ from both sides, so $L$ is a based homotopy; $L_{0}=(\alpha*\beta)*\gamma$ and $L_{1}=\alpha*(\beta*\gamma)$.
:::

:::

::: {.pf-step #inverse}
The reversal $\alpha^{-1}(t)=\alpha(1-t)$ satisfies $\alpha*\alpha^{-1}\simeq e\simeq\alpha^{-1}*\alpha$ through based loops.

::: pf-proof
$\alpha*\alpha^{-1}$ traverses $\alpha$ and then back along it, that is $(\alpha*\alpha^{-1})(t)=\alpha(g(t))$ with $g(t)=\min(2t,2-2t)$. The homotopy $H(t,s)=\alpha\bigl((1-s)g(t)\bigr)$ is continuous, satisfies $H(\cdot,0)=\alpha*\alpha^{-1}$ and $H(\cdot,1)=e$, and is based at every stage because $H(0,s)=\alpha(0)=H(1,s)$. The other composite is handled the same way with $g$ replaced by $1-g$.
:::

:::

::: {.pf-step}
$\Omega X$ is an H-space with multiplication the composition of loops; it is moreover associative and has homotopy inverses, which the definition of an H-space does not require.

::: pf-proof
Step [](#hspace){.pf-ref} is the assertion of the exercise. Steps [](#assoc){.pf-ref} and [](#inverse){.pf-ref} give the extra structure, recorded because the exercise's multiplication has it; neither is used in step [](#hspace){.pf-ref}, whose hypothesis is only the unit condition.
:::

:::

:::

:::
