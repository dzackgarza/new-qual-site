# Rubric for Koebe–Bieberbach Hard Proof Eval (E-SS3.PR-1)

This rubric grades solutions **without reference to model outputs**. It is derived solely from the problem statement in `HARD-PROOF-EVAL.md` and the canonical proof outline in `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-1.md`. Use it blind to the eval files in this directory.

Problem: Koebe–Bieberbach radius theorem for normalized univalent functions `f:D→C` with `f(0)=0`, `f'(0)=1`, `f` injective ⇒ `D_{1/4}(0) ⊂ f(D)` and `1/4` sharp, via seven steps (a)–(g).

Total: 100 points. Partial credit per bullet. No credit for a step that asserts the conclusion without proof or that uses Cauchy's theorem where the problem forbids it in early parts.

---

## (a) No uniform r without restrictions (5 points)

- [2] Exhibit explicit `fn` holomorphic on `D` with `fn(0)=0` and a point in `D_r(0)` omitted (canonical `fn(z)=z/n` omits `1/n`, or equivalent). Must compute `fn(D)=D_{1/n}(0)`.
- [1] Compute `fn'(0)` correctly (`1/n → 0`) and note dependence on `n`.
- [2] Conclude no fixed `r>0` works for all such `f` (quantifier argument: for any `r` pick `n>1/r`).

Fail: chooses `fn` that does not satisfy `fn(0)=0` or that does not omit a point of `D_r(0)`.

## (b) Even with f'(0)=1 no uniform r (5 points)

- [2] Exhibit `fε(z)=ε(e^{z/ε}-1)` and verify `fε(0)=0`, `fε'(0)=1`.
- [2] Show `fε(D)` omits `-ε` (since `e^{z/ε}≠0`).
- [1] Conclude no uniform `r` (for any `r` pick `ε<r`).

Fail: omits the verification that `fε` omits a point of `D_r(0)` or that `fε'(0)=1`.

## (c) Area theorem Σ n|cn|² ≤1 (20 points)

This is the technical core. Grade strictly.

- [4] Set up: `h(z)=1/z + c0 + Σ_{n≥1} cn z^n` analytic and injective on `0<|z|<1` with simple pole at `0`; for `0<ρ<1` the curve `γρ(t)=h(ρ e^{it})` is simple closed (injective on `|z|=ρ`, derivative nonzero). Define `Aρ = area( C \ h(D_ρ\{0\}) )` (bounded complement).
- [6] Derive `Aρ = π( ρ^{-2} - Σ_{n≥1} n|cn|² ρ^{2n} )` via `A = -(1/2i)∮ \bar w dw = -(1/2i)∫_0^{2π} \bar h h_t dt` or Green's theorem, showing the cross terms: compute `∫ \bar h h_t = 2π i( Σ n|cn|² ρ^{2n} - ρ^{-2})` with explicit Fourier orthogonality (only diagonal `n=m` survives, `c0` drops). Must handle `ρ^{-1}e^{it}` term and ` -iρ^{-1}e^{-it}` term correctly and get sign correct.
- [4] Use `Aρ ≥ 0` to get `Σ n|cn|² ρ^{2n} ≤ ρ^{-2}` for all `ρ<1`.
- [4] Pass `ρ→1^-` to get `Σ n|cn|² ≤1` (monotone convergence or `limsup`, not just pointwise limit without justification). Must not claim `Aρ→0` without proof.
- [2] Clarity: state that injectivity gives Jordan curve, so area formula applies; note `h` univalent ⇒ `h'≠0` on `D^*`.

Partial: 8/20 if area formula stated without derivation but inequality correctly obtained; 0/20 if inequality asserted without area argument.

## (d) Square-root g with g²(z)=f(z²) (15 points)

- [4] Show `f(z)/z` is holomorphic and nowhere vanishing on `D` (use `f(0)=0`, `f'(0)=1` ⇒ `f(z)=z(1+O(z))` and `f(z)≠0` for `z≠0` by injectivity).
- [4] Existence of holomorphic `ψ` with `ψ² = f(z)/z` and `ψ(0)=1` (simply connected `D`, nowhere-vanishing ⇒ holomorphic logarithm/square root). Must not just assert existence.
- [3] Define `g(z)=z ψ(z²)` and verify `g²(z)=f(z²)`, `g(0)=0`, `g'(0)=1` (`g'(0)=ψ(0)=1`).
- [4] Prove `g` is injective (use `g² = f∘(z↦z²)` and oddness: `g(-z)=-g(z)`; if `g(z1)=g(z2)` then `f(z1²)=f(z2²)` ⇒ `z1²=z2²`, then `z1=±z2` and oddness forces `z1=z2` unless `z1=z2=0`). Must handle `z=0` separately.

Fail: defines `ψ` without justifying simply-connected or `f(z)/z≠0`; or claims `g` injective because `f` is, without handling the `z↦z²` 2-to-1.

## (e) Coefficient bound |a2|≤2 and equality case (20 points)

- [4] Write `1/g(z)=1/z + b0 + b1 z + …`. Show `g(z)=z + b2 z³+…` odd ⇒ `1/g(z)=1/z - b2 z + …` so the `c1` coefficient of `1/g` is `-b2`. Must compute correctly.
- [4] Relate `b2 = a2/2` via `ψ(z)=1 + (a2/2)z + …` and `g(z)=z ψ(z²)`.
- [6] Apply (c) to `1/g` to get `Σ n|cn|² ≤1` ⇒ in particular `|b2|≤1` ⇒ `|a2|≤2`. Must state that `1/g` is of the form required for (c) (injective on `D^*` with simple pole at `0`).
- [6] Equality characterization: `|a2|=2` ⇒ `|b2|=1` ⇒ `Σ n|cn|² =1` with `|c1|=1` forces `1/g(z)=1/z + e^{iθ}z` (equality in area theorem forces all other `cn=0` and `|c1|=1`; must argue via `Aρ→0` and that `|c1|=1` forces the image to be `C` minus a slit, i.e., the extremal function). Then `g(z)=z/(1+e^{iθ}z²)` and `f(z)=z/(1+e^{iθ}z)²` up to rotation, i.e., Koebe `z/(1-e^{iθ}z)²` after `θ↦θ+π`. Must not just assert equality case without using (c).

Partial: 10/20 if bound `|a2|≤2` proved but equality case hand-waved; 0/20 if `|a2|≤2` asserted via known Bieberbach without using (c)–(d).

## (f) Two omitted values bound |z1−z2|≤4 (15 points)

- [5] Setup: `h(z)=1/z + c0 + Σ cn z^n` injective on `D^*` avoiding `z1,z2` ⇒ for each `j`, `hj(z)=h(z)-zj` is of the same form `1/z + (c0−zj)+…` and `1/(h(z)-zj)` is not needed; instead apply (c) to `1/(h(z)-zj)` is wrong. Correct route: consider `kj(z)=1/(h(z)-zj)` is **not** of the form `1/z+…` (it has a zero, not a pole). The standard lemma uses `hj` itself: `hj(z)=h(z)-zj =1/z + (c0−zj)+…` still satisfies (c) hypotheses (injective, simple pole at `0`, avoids `0`? Wait `hj` avoids `0`? Actually `h` avoids `z1,z2`, so `hj` avoids `0` is false; need the clean version: define `Hj(z)=1/(h(z)-zj)` has a simple **zero** at `0`; then consider `1/Hj(z)=h(z)-zj` which **does** have a simple pole and satisfies (c). The usual proof then looks at the second coefficient of `1/Hj` after writing `1/Hj` as `1/z+…` and uses that the `c1` coefficient is bounded. The clean grading: the solver must correctly identify which function has a pole and to which function (c) applies, and must correctly compute the relevant coefficient.

  Accept either correct chain: (i) apply (c) to `h(z)-zj` to bound its `c1` (which is same as `c1` of `h`), or (ii) apply (c) to `1/(h(z)-zj)` after shifting to pole form via `z↦1/z` trick, but must be coherent. Do not give full credit for applying (c) to a function that does not have a simple pole at `0`.

- [5] Show `|z1−z2|≤4` via coefficient comparison: the `c0` shift gives `|z1−z2| = |(c0−z1)-(c0−z2)|` and the bound comes from `|c1|≤1` for each `hj` and the relation between the second coefficient of `1/(h−zj)` and `zj`. The cleanest check: the second coefficient of `1/(h(z)-zj)` expanded as `z - (c0−zj)z² + …` is `-(c0−zj)`; then `| (c0−z1) - (c0−z2) | = |z2−z1| ≤ |c0−z1|+|c0−z2| ≤ 2` is **wrong** by factor 2; the correct bound is `4` and requires using the `c1` of `1/(h−zj)` or the standard `|c1|≤1` for both `hj` and then `|z1−z2|≤ |c0^{(1)}-c0^{(2)}| ≤ 4` via the area theorem applied to `1/(h−zj)`'s reciprocal's second coefficient. The grader must check the arithmetic that yields `4`, not `2`. Award 5/5 only if the final inequality is `≤4` with a coherent coefficient identification.

- [5] No gaps: must state that `h` injective and avoiding `z1,z2` implies each `h(z)-zj` is injective and of the required `1/z+…` form (pole at `0` remains simple). Must not confuse zero vs pole.

Partial: 7/15 if idea correct (apply (c) to `h−zj` and compare) but coefficient arithmetic off by factor; 0/15 if `|z1−z2|≤4` asserted without using (c).

## (g) Completion to r=1/4 (10 points)

- [4] Suppose `f` (normalized univalent) omits `w` with `|w|<1/4`. Then `1/f` has simple pole at `0` with `1/f(z)=1/z - a2 + …` (or `1/z + …`), is injective on `D^*`, and avoids `0` and `1/w`.
- [4] Apply (f) to `h=1/f` with `z1=0, z2=1/w` to get `|1/w| = |0-1/w| ≤4` ⇒ `|w|≥1/4`, contradiction.
- [2] Conclude `D_{1/4}(0)⊂f(D)` and note sharpness via Koebe `z/(1-z)²` omitting `-1/4`.

Fail: omits the step that `1/f` satisfies the hypotheses of (f) (simple pole at `0`, injective on `D^*`).

---

## Overall presentation (10 points, holistic)

- [3] Logical flow: steps (a)–(g) build correctly, no circularity (e.g., not using (g) to prove (c)).
- [3] Rigor: quantifiers correct (`for all r`, `exists fn`), edge cases handled (`z=0` for `g`, `ρ→1` limit justified), no hand-waving `clearly`.
- [2] Notation: consistent `D`, `D_ρ`, `H`, `h`, `f`, `g`, `ψ` defined before use.
- [2] Use of hints: follows hints where given but may give equivalent argument; does not ignore hint and substitute an unproven external theorem (e.g., not citing de Branges for `|a2|≤2` without (c)–(d)).

Deductions:

- Major gap that breaks a step: −100% of that step.
- Minor computational slip that does not break logic (e.g., missing factor `i` in area integral but final inequality correct): −1 point on that step.
- Asserting area theorem without proof: cap (c) at 8/20.
- Using `f(z)/z` square root without noting simply connected or `f(z)≠0` for `z≠0`: cap (d) at 8/15.

---

## Grading scale

- 90–100: Complete, rigorous, all seven steps with equality characterization; publishable.
- 75–89: All steps present, minor gaps in (c) or (f) coefficient arithmetic.
- 60–74: Core theorem proved but (c) or (e) equality case incomplete.
- 40–59: (a)–(d) correct, (e)–(g) hand-waved or missing.
- <40: Multiple steps missing or major logical errors.

---

## How to use this rubric without looking at evals

Grade each file in `evals/HARD-PROOF-EVAL/` blind to the model name: open the file, hide the header `Model:`, and score (a)–(g) plus overall against this rubric. Record subscores in a `SCORES.md` table `| File | (a) | (b) | (c) | (d) | (e) | (f) | (g) | Overall | Total | Notes |`. Do not adjust the rubric after seeing any model output.

Sources: Problem verbatim from `HARD-PROOF-EVAL.md` (which is verbatim `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-1.md`); canonical proof outline from the same source's `::: {.solution}`; area theorem and equality case as in standard Koebe proof.
