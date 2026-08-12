# Direct review of previously dropped source rows

## Review boundary

This is a manual direct review of every row currently marked `dropped` in `sources/migration-ledger.jsonl`. The review reads each pinned source object, records its Git object ID and byte length, and records the finding that supports the disposition.
The review does not add a verifier, replay tool, or migration automation.

The review covers 367 rows from these pinned source revisions:

- `qual-wiki`: `3fe1f58fdf800209c5ad243c91411bc0ee40cc7c`

- `qual-review-and-solutions`: `590a8929b2326cc770a246e934ab36fb30b0c7ab`

- `make-me-a-qual`: `beba581e5b32f54ff469ed603a0885d51591e5fc`

- `math-flashcards`: `69cecc401981fb2f897a6a3c29feb869d811013c`

The direct findings are homogeneous only within each section below.
Every source path is named.

## qual-wiki — editor config (100 rows)

Direct read: editor, plugin, theme, workspace, or ignore configuration; no authored mathematical, bibliographic, provenance, or figure payload.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `.gitignore` | `859f705bdb6ee2bbbbb24fc91a065ddbbe77666e` | 2684 |
| `.obsidian/app.json` | `b0b83231501a9fd784e9899f31aa52bbc1ea40a3` | 7136 |
| `.obsidian/appearance.json` | `f7bd107b68199fa88f0320a854efbb27ebd3e827` | 121 |
| `.obsidian/community-plugins.json` | `98773a1e33eb3d859afed44283b4d95b29447b05` | 525 |
| `.obsidian/core-plugins.json` | `a196e2d8ba6be9b99a0ddf92b87a15dbcaf64561` | 277 |
| `.obsidian/file-recovery.json` | `286ebd7659441abd72fa0241abeab68f802521e1` | 44 |
| `.obsidian/graph.json` | `e967913062e5c90e1d75a5e6523a77cc88965201` | 992 |
| `.obsidian/hotkeys.json` | `e35493c0398637c0c4aa5b4a1a3875a2586b9dab` | 1280 |
| `.obsidian/page-preview.json` | `cd434618d2855bae71914ec200fb4497c935a88d` | 21 |
| `.obsidian/plugins/consistent-attachments-and-links/data.json` | `ee902d48d044d7198724eb4255784c50a2c24a3c` | 401 |
| `.obsidian/plugins/consistent-attachments-and-links/main.js` | `266d80b9d929e7ba90b699418914bf4dff8eb67c` | 340396 |
| `.obsidian/plugins/consistent-attachments-and-links/manifest.json` | `ad7b6f7ba8a7b6ced8110e768d17e1876856f332` | 316 |
| `.obsidian/plugins/cycle-through-panes/main.js` | `f5c57f971eea43aba3f422690c979138b0ddc147` | 62592 |
| `.obsidian/plugins/cycle-through-panes/manifest.json` | `fdeaf762d0f32484e8e4ac2451392894409bcf95` | 355 |
| `.obsidian/plugins/dataview/main.js` | `0d56b8c7a5a4d052115a99a41c5183d7d98b9f86` | 2380041 |
| `.obsidian/plugins/dataview/manifest.json` | `ce1f93c67cc17c06f90152dedfc299fdf3126591` | 291 |
| `.obsidian/plugins/dataview/styles.css` | `3a204888d3bc10c00729e567680ea526fe4b5dfd` | 3106 |
| `.obsidian/plugins/find-unlinked-files/data.json` | `d7087c161c1ce8e8985d69294590e580030006d5` | 674 |
| `.obsidian/plugins/find-unlinked-files/main.js` | `1e914b052883867f40870a4bfeb49d4d105e424a` | 165140 |
| `.obsidian/plugins/find-unlinked-files/manifest.json` | `9b3fb574d263e40704ba321d0bb664b4c033e9ef` | 346 |
| `.obsidian/plugins/folder-note-plugin/main.js` | `99575e57c74dd7c59a5d84e54992ee1234b7a824` | 1079682 |
| `.obsidian/plugins/folder-note-plugin/manifest.json` | `835549668209538ebb2b4b56685f4549636914ae` | 288 |
| `.obsidian/plugins/folder-note-plugin/styles.css` | `abe59dfeaadf67df1ae22adc093be6ccfe5e5872` | 4835 |
| `.obsidian/plugins/juggl/graph.css` | `eb209d36c48b98dcc3b21ae7790632ad4e028e7e` | 83 |
| `.obsidian/plugins/juggl/main.js` | `12ab7e32649194ef21519421bc7a5e89de77c8dc` | 2838981 |
| `.obsidian/plugins/juggl/manifest.json` | `058b7efad46944ea3aa370c2b294a09ff8bc6c13` | 282 |
| `.obsidian/plugins/juggl/styles.css` | `c3b75d1c1575511da34be7be29f488f54cfe64bc` | 3624 |
| `.obsidian/plugins/mrj-text-expand/main.js` | `bae38a3e2f267115da542b4b3748403f2d36b60b` | 167718 |
| `.obsidian/plugins/mrj-text-expand/manifest.json` | `3d537025aff7ca932abb678e123e7602883ec724` | 243 |
| `.obsidian/plugins/obsidian-charts/main.js` | `fb46650aa0ceb79ee0c7c0bf369cf1306ecdbb82` | 329452 |
| `.obsidian/plugins/obsidian-charts/manifest.json` | `f11797a1e1f18690d3e1d70e73bedbcc7fbd5917` | 289 |
| `.obsidian/plugins/obsidian-charts/styles.css` | `ae9c32b020e949100cca15f908a00ff1536d85a2` | 587 |
| `.obsidian/plugins/obsidian-chartsview-plugin/main.js` | `b9317be5407928dc1facf19cb976ef111aa4d438` | 2483603 |
| `.obsidian/plugins/obsidian-chartsview-plugin/manifest.json` | `81a3fc1f4c1a59bfd5b8a1254d91392c9d622354` | 322 |
| `.obsidian/plugins/obsidian-chartsview-plugin/styles.css` | `85e1186dd4b2c357b15c5e91fcdcb16a3348071e` | 1103 |
| `.obsidian/plugins/obsidian-citation-plugin/data.json` | `da79ae50422837eb88e11b4ca43001136510be65` | 400 |
| `.obsidian/plugins/obsidian-citation-plugin/main.js` | `a20a9696012c0cae2096c8e8a0d7a497321a51c1` | 5479001 |
| `.obsidian/plugins/obsidian-citation-plugin/manifest.json` | `caaf297218e0c4506a464c60606fd26c269eaaff` | 276 |
| `.obsidian/plugins/obsidian-citation-plugin/styles.css` | `729a0d16e42d6afa23c3452d5a0d69ee571e5b0f` | 2096 |
| `.obsidian/plugins/obsidian-dangling-links/data.json` | `96355af1dcbf8097a603f9556093f54c80961eee` | 117 |
| `.obsidian/plugins/obsidian-dangling-links/main.js` | `cac4e4bde886f4ed3a17b9dcb30f3f49fb1a64be` | 415018 |
| `.obsidian/plugins/obsidian-dangling-links/manifest.json` | `fdb1286daafb274a58624e9dbd1138036ff0a4dd` | 305 |
| `.obsidian/plugins/obsidian-dangling-links/styles.css` | `48ee07c661d31b25a0eb3b7c80f1317295170cd9` | 416 |
| `.obsidian/plugins/obsidian-emoji-toolbar/main.js` | `58961a801e6c111700c8dc2e997df3f948985b98` | 2520271 |
| `.obsidian/plugins/obsidian-emoji-toolbar/manifest.json` | `088e6d74bb168c98eacc842cfcfb1e5aa009c1e6` | 279 |
| `.obsidian/plugins/obsidian-emoji-toolbar/styles.css` | `9b0eb339faa2f9d8909439d83c4b2375246a50f8` | 10187 |
| `.obsidian/plugins/obsidian-extract-pdf-highlights/main.js` | `fea43bc8c20782ed4f41cb8ab2c1ac052989e4b5` | 13300615 |
| `.obsidian/plugins/obsidian-extract-pdf-highlights/manifest.json` | `86f20aadc62e8e3c788dcee7e26e226c329b9b75` | 329 |
| `.obsidian/plugins/obsidian-extract-pdf-highlights/styles.css` | `79a9626b5500c171eaa6dbeef1681e91f922e9dc` | 6 |
| `.obsidian/plugins/obsidian-latex/main.js` | `9b5f9f16bac5cd540a1112b4ce31a3ac01db5d74` | 32417 |
| `.obsidian/plugins/obsidian-latex/manifest.json` | `dfda56612c32e7468b045612510baf45dfd5e25d` | 357 |
| `.obsidian/plugins/obsidian-mind-map/main.js` | `6bcab4a79269eac2345ab26e65a06876a481a22b` | 4003625 |
| `.obsidian/plugins/obsidian-mind-map/manifest.json` | `97a9af843553b402c0cb5a317749eafbb30baac2` | 187 |
| `.obsidian/plugins/obsidian-outliner/main.js` | `99c7398bbf8aa28b5a3c6444e42a32f1a0967d72` | 361052 |
| `.obsidian/plugins/obsidian-outliner/manifest.json` | `7934f6175595fc3ccd81f6eb6015de1a8a5a837e` | 284 |
| `.obsidian/plugins/obsidian-outliner/styles.css` | `c2792286c50456781715222476711f98940b6c51` | 1403 |
| `.obsidian/plugins/obsidian-pandoc/data.json` | `2f49bb6fea997bcaa218077ef2526681f3eae067` | 359 |
| `.obsidian/plugins/obsidian-pandoc/main.js` | `66b89d17c7c4c482a31942e9325a653ac16bdb8d` | 324162 |
| `.obsidian/plugins/obsidian-pandoc/manifest.json` | `8e570d26d460e8b372b766dadcd420c61886e227` | 361 |
| `.obsidian/plugins/obsidian-pandoc/styles.css` | `98facd9f49bee18f79557ea091958fe3b5f52719` | 42 |
| `.obsidian/plugins/obsidian-spaced-repetition/main.js` | `fb0eb9f3fb9c0329207e6396b4090e629520a1e2` | 1140100 |
| `.obsidian/plugins/obsidian-spaced-repetition/manifest.json` | `7a1fa64cacb45cec7974acd0c9fed6952596f3d3` | 377 |
| `.obsidian/plugins/obsidian-spaced-repetition/styles.css` | `70c339f28c8c42364c15766a310ff553d10bd168` | 1941 |
| `.obsidian/plugins/obsidian-tracker/main.js` | `cf650b4af73d6d1b2e28e1681c4d292d29a9dbcf` | 1470534 |
| `.obsidian/plugins/obsidian-tracker/manifest.json` | `eae5e4dbc7dc1d0aa8b4b54703828a37426d1c07` | 241 |
| `.obsidian/plugins/obsidian-tracker/styles.css` | `9cd8b4caffff016425410b0ad365f8b05631f5cb` | 3283 |
| `.obsidian/plugins/obsidian-vault-changelog/data.json` | `5fa6e58c3669df5e4219e7d35c24ae33b3364d58` | 100 |
| `.obsidian/plugins/obsidian-vault-changelog/main.js` | `79dec935ad2825401ef62bfef5e5a0eeaf908448` | 48049 |
| `.obsidian/plugins/obsidian-vault-changelog/manifest.json` | `60aa2daabfe7f1fbd039f4c15fb9ffa40ae1f3e5` | 291 |
| `.obsidian/plugins/recent-files-obsidian/data.json` | `453782fe8f43c21d1a3c76da64101548268d9e46` | 6121 |
| `.obsidian/plugins/recent-files-obsidian/main.js` | `703f04079d1b9a3b5844ecd3d5a55babec878b38` | 151559 |
| `.obsidian/plugins/recent-files-obsidian/manifest.json` | `e82cc747e650e74b6e3cb5d64f892c6ca1135183` | 263 |
| `.obsidian/plugins/recent-files-obsidian/styles.css` | `87e7ae7d6af684de47be6394bcb6bc3459c1bbbe` | 519 |
| `.obsidian/plugins/sliding-panes-obsidian/main.js` | `7596b696ee9302f653a35dc481a8cf493222dab1` | 126968 |
| `.obsidian/plugins/sliding-panes-obsidian/manifest.json` | `3ef7598806391d935cd74d9d5f3aab9706bf0180` | 339 |
| `.obsidian/plugins/sliding-panes-obsidian/styles.css` | `981c94198025ffe1ef19667f0e6d69ebad30f7fe` | 7616 |
| `.obsidian/plugins/smart-random-note/main.js` | `27abde3a0ac38cbf1a3cfe6ab3dbd63e84e0f009` | 173714 |
| `.obsidian/plugins/smart-random-note/manifest.json` | `e94395619d1ebddbde0741dea687d9ea49a24627` | 249 |
| `.obsidian/plugins/table-editor-obsidian/data.json` | `90094659b6f8f38d1d28eb99e2c9e66dfb056778` | 94 |
| `.obsidian/plugins/table-editor-obsidian/main.js` | `81956cc042e7624c4c8373181169d9252f3d4dd7` | 2772931 |
| `.obsidian/plugins/table-editor-obsidian/manifest.json` | `ff201470a10293cf30e8b80787999538629c35a6` | 369 |
| `.obsidian/plugins/table-editor-obsidian/styles.css` | `089b8cdda4ceebbfba1fca170f06a2d7b8a8d8f3` | 1751 |
| `.obsidian/plugins/tag-wrangler/main.js` | `27be473d9348643c9962767d33640ae54e5df310` | 114082 |
| `.obsidian/plugins/tag-wrangler/manifest.json` | `545928900659eadb9e4e9e954464c669368c4a50` | 272 |
| `.obsidian/plugins/tag-wrangler/styles.css` | `198e205146d383dbf085b65f79b4ab8ccb833ecc` | 3230 |
| `.obsidian/plugins/templater-obsidian/data.json` | `f8cc35cb682552c727a6fed9b3a415c45831fc84` | 510 |
| `.obsidian/plugins/templater-obsidian/main.js` | `322625380dfcdabaa54e574dd626b15d17ab4a9b` | 287625 |
| `.obsidian/plugins/templater-obsidian/manifest.json` | `70cf5959acb49950c74f7a16cc182a448813dfd7` | 272 |
| `.obsidian/plugins/templater-obsidian/styles.css` | `207db95002fb37d73200ccbee2385555d29e2019` | 5593 |
| `.obsidian/plugins/wikilinks-to-mdlinks-obsidian/main.js` | `17548c620e8dcddd14d143f4a9d5c1651cdebfdb` | 33464 |
| `.obsidian/plugins/wikilinks-to-mdlinks-obsidian/manifest.json` | `a5a14166bc0ddf93324fb04d57f7f5bee4cfa57f` | 305 |
| `.obsidian/starred.json` | `43950404e7869de602869aba5f8cd35a8ef14380` | 1015 |
| `.obsidian/themes/Clean theme.css` | `dcec21148a7fe50463f4752c2a081c187acab87d` | 7777 |
| `.obsidian/themes/Deep Work.css` | `86711e01cf2adf5093d1b775dcd9815fb77ab290` | 27082 |
| `.obsidian/themes/Notation.css` | `923454e1117fe0da20b28dd2654209d4147e5783` | 21699 |
| `.obsidian/themes/Warmth.css` | `8fc2c91623f2b890d17dd1c741a08d9044b4275a` | 9358 |
| `.obsidian/workspace` | `0de8cadd113e5b7bd4f93cd7c356d81363afb2ce` | 8046 |
| `.obsidian/workspace.json` | `2452b0472256b5301c93e074d841f2352492f62d` | 7675 |
| `.obsidian/workspaces.json` | `9e26dfeeb6e641a33dae4961196235bdb965b21b` | 2 |
| `.obsidian/zk-prefixer.json` | `eeefe262d3d1f43a07409ff475644fb100a6c92d` | 83 |

## qual-wiki — non-content file (no ext) (63 rows)

Direct read: repository identifier only.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `.sparkleshare` | `67370846a7dfab2955c655258751b6279143f2bf` | 64 |
| `00_Prelims/Problems/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/020_Groups/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/040_Rings/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/060_Galois/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/060_Galois/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/080_Modules/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/080_Modules/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/100_Linear_Algebra/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/Combined/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/Final/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/Midterm/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/PSet 1/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/PSet 10/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/PSet 2/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/PSet 3/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/PSet 4/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/PSet 5/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/PSet 6/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/PSet 6/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/PSet 7/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/PSet 8/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/500_Exercises/PSets/PSet 9/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `10_Algebra/600_Qual_Questions_UGA/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `10_Algebra/600_Qual_Questions_UGA/figures` | `1568855e25c7dcd6565405ac754f7a9c5f8c1f82` | 24 |
| `10_Algebra/TexDocs/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `10_Algebra/TexDocs/Makefile` | `1322c36aa079cfcf2c265c76b2c0e98100f7c037` | 2887 |
| `10_Algebra/TexDocs/figures` | `8887e4674fc8c50b4bfa37efe3f10e90ab615841` | 18 |
| `10_Algebra/TexDocs/sections` | `9fd9ade740d3f6fc9a1d9dfad461871c1f3017c5` | 25 |
| `20_Real_Analysis/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `20_Real_Analysis/010_Measure_Theory/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `20_Real_Analysis/200_Appendices/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `20_Real_Analysis/200_Appendices/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `20_Real_Analysis/600_Qual_Questions_UGA/figures` | `1568855e25c7dcd6565405ac754f7a9c5f8c1f82` | 24 |
| `20_Real_Analysis/TexDocs/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `20_Real_Analysis/TexDocs/Makefile` | `d7f0a48a8810d8d26b5a07d5464b117e27b021e0` | 2985 |
| `20_Real_Analysis/TexDocs/figures` | `8887e4674fc8c50b4bfa37efe3f10e90ab615841` | 18 |
| `20_Real_Analysis/TexDocs/sections` | `9fd9ade740d3f6fc9a1d9dfad461871c1f3017c5` | 25 |
| `20_Real_Analysis/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `30_Complex_Analysis/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `30_Complex_Analysis/010_Basics/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `30_Complex_Analysis/030_Zeros_and_Poles/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `30_Complex_Analysis/050_Conformal_Maps/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `30_Complex_Analysis/900 Unsorted/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `30_Complex_Analysis/999_Quals/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `30_Complex_Analysis/999_Quals/figures/figures` | `1568855e25c7dcd6565405ac754f7a9c5f8c1f82` | 24 |
| `30_Complex_Analysis/TexDocs/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `30_Complex_Analysis/TexDocs/Makefile` | `b5810bc737c9dd16a3ea9856f72825aef598f42b` | 3236 |
| `30_Complex_Analysis/TexDocs/figures` | `8887e4674fc8c50b4bfa37efe3f10e90ab615841` | 18 |
| `30_Complex_Analysis/TexDocs/sections` | `00459b98c4465d904b6ef446b62a02e64fb57037` | 12 |
| `40_Topology/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `40_Topology/020_Point_Set/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `40_Topology/060_Homology/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `40_Topology/200_Appendices/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `40_Topology/500_Exercises/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `40_Topology/650_UCSD_Qual_Questions/Quals/assets/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `40_Topology/999_Extra_Problems/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `40_Topology/TexDocs/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `40_Topology/TexDocs/Makefile` | `5a126f1eb4e4ac3ab35f10ad471647db5481d67e` | 2892 |
| `40_Topology/TexDocs/figures` | `8887e4674fc8c50b4bfa37efe3f10e90ab615841` | 18 |
| `40_Topology/TexDocs/sections` | `ef2db3b0e683dddb453d369f3f256d00cc827edd` | 25 |
| `Workshops/Algebra/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |

## qual-wiki — non-content file (.html) (1 rows)

Direct read: zero-byte generated HTML file.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `10_Algebra/TexDocs/QualAlgebra.html` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | 0 |

## qual-wiki — non-content file (.sh) (2 rows)

Direct read: build or text-normalization shell script only; no authored corpus payload.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `emanote_preview.sh` | `19ed0070a4efbc9a4149f8336fee316c94e88668` | 2525 |
| `emanote_stripmacro.sh` | `850fb8dfe038d4bc29dc9a630774a4754707511f` | 2286 |

## qual-wiki — non-content file (.sty) (1 rows)

Direct read: one-line external macro-path pointer; no local macro definitions.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `preamble.sty` | `0228d7b68b7bf98529fe07ed578c135b77a054eb` | 39 |

## qual-review-and-solutions — editor config (80 rows)

Direct read: editor, plugin, theme, workspace, or ignore configuration; no authored mathematical, bibliographic, provenance, or figure payload.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `.gitignore` | `859f705bdb6ee2bbbbb24fc91a065ddbbe77666e` | 2684 |
| `.obsidian/app.json` | `b54a9369919b3443083333a09c14c0e6f0c6033b` | 6393 |
| `.obsidian/appearance.json` | `314a0072cb3ab22caf6416c93423159fca13d983` | 97 |
| `.obsidian/community-plugins.json` | `f3cc90d230a29d1ac6d13ac6511a5931efa4cd61` | 360 |
| `.obsidian/core-plugins.json` | `8168cc3410bd086508af07ebd55affdbc1e1ae72` | 304 |
| `.obsidian/file-recovery.json` | `286ebd7659441abd72fa0241abeab68f802521e1` | 44 |
| `.obsidian/graph.json` | `eaab15ca39ccf4203156d47ee87ade9e42022d74` | 992 |
| `.obsidian/hotkeys.json` | `375c81a960292eebfc513a01478e1f747216a6a3` | 1171 |
| `.obsidian/page-preview.json` | `cd434618d2855bae71914ec200fb4497c935a88d` | 21 |
| `.obsidian/plugins/consistent-attachments-and-links/data.json` | `af9c21f5d555c4fa606b6f1855becd1886beafea` | 400 |
| `.obsidian/plugins/consistent-attachments-and-links/main.js` | `130545905b94fe87c79f59a41414d5de91ea4a26` | 317836 |
| `.obsidian/plugins/consistent-attachments-and-links/manifest.json` | `fa9acb4339626fa1145f809b81b96b795103891b` | 322 |
| `.obsidian/plugins/cycle-through-panes/main.js` | `9e520a0561138204e50f67798ee209c7e5ae39a9` | 32440 |
| `.obsidian/plugins/cycle-through-panes/manifest.json` | `3116ef79598155ddcd0afa9d8892ecf4df8c58d0` | 352 |
| `.obsidian/plugins/dataview/main.js` | `98f5b5349e9793df3c781e8fb124272f71338566` | 1663243 |
| `.obsidian/plugins/dataview/manifest.json` | `37862019dd8ac5e63b1851e91ab04b9bcd8e1c31` | 290 |
| `.obsidian/plugins/dataview/styles.css` | `9650924dc1ae5d63526c6e29c876c3244db4d374` | 1643 |
| `.obsidian/plugins/find-unlinked-files/data.json` | `d7087c161c1ce8e8985d69294590e580030006d5` | 674 |
| `.obsidian/plugins/find-unlinked-files/main.js` | `5a0b787157dc992ca9e8d7c3b3eb40aa3c2b7883` | 120962 |
| `.obsidian/plugins/find-unlinked-files/manifest.json` | `a9cbdc8194d3cf0c57c91ca5ddc63572a304a72f` | 349 |
| `.obsidian/plugins/folder-note-plugin/main.js` | `99575e57c74dd7c59a5d84e54992ee1234b7a824` | 1079682 |
| `.obsidian/plugins/folder-note-plugin/manifest.json` | `835549668209538ebb2b4b56685f4549636914ae` | 288 |
| `.obsidian/plugins/folder-note-plugin/styles.css` | `abe59dfeaadf67df1ae22adc093be6ccfe5e5872` | 4835 |
| `.obsidian/plugins/juggl/graph.css` | `eb209d36c48b98dcc3b21ae7790632ad4e028e7e` | 83 |
| `.obsidian/plugins/juggl/main.js` | `15b231031ccf794590825130d6f76cf02df649a8` | 13261296 |
| `.obsidian/plugins/juggl/manifest.json` | `cbd33bc8301b9e0f26e126c5a0375811583c435b` | 282 |
| `.obsidian/plugins/juggl/styles.css` | `e22e4f2c156c0c49d79843a5fba6fd83698722d0` | 3545 |
| `.obsidian/plugins/obsidian-citation-plugin/data.json` | `da79ae50422837eb88e11b4ca43001136510be65` | 400 |
| `.obsidian/plugins/obsidian-citation-plugin/main.js` | `6fe1b0d62f22d2088b8fc878e6097935b03f29c8` | 5473439 |
| `.obsidian/plugins/obsidian-citation-plugin/manifest.json` | `ab2362fa026e023fb9e4662182e16d4a8cd26686` | 277 |
| `.obsidian/plugins/obsidian-citation-plugin/styles.css` | `729a0d16e42d6afa23c3452d5a0d69ee571e5b0f` | 2096 |
| `.obsidian/plugins/obsidian-dangling-links/data.json` | `96355af1dcbf8097a603f9556093f54c80961eee` | 117 |
| `.obsidian/plugins/obsidian-dangling-links/main.js` | `cac4e4bde886f4ed3a17b9dcb30f3f49fb1a64be` | 415018 |
| `.obsidian/plugins/obsidian-dangling-links/manifest.json` | `fdb1286daafb274a58624e9dbd1138036ff0a4dd` | 305 |
| `.obsidian/plugins/obsidian-dangling-links/styles.css` | `48ee07c661d31b25a0eb3b7c80f1317295170cd9` | 416 |
| `.obsidian/plugins/obsidian-emoji-toolbar/main.js` | `26d51d48130af9159145f2ca9121c86564d35758` | 470087 |
| `.obsidian/plugins/obsidian-emoji-toolbar/manifest.json` | `1e417b06e54a10e0c3cdced911c477c7a9e53f28` | 279 |
| `.obsidian/plugins/obsidian-emoji-toolbar/styles.css` | `057b181224515393b3e3122ede14e74f524f49bd` | 122 |
| `.obsidian/plugins/obsidian-extract-pdf-highlights/main.js` | `fea43bc8c20782ed4f41cb8ab2c1ac052989e4b5` | 13300615 |
| `.obsidian/plugins/obsidian-extract-pdf-highlights/manifest.json` | `86f20aadc62e8e3c788dcee7e26e226c329b9b75` | 329 |
| `.obsidian/plugins/obsidian-extract-pdf-highlights/styles.css` | `79a9626b5500c171eaa6dbeef1681e91f922e9dc` | 6 |
| `.obsidian/plugins/obsidian-latex/main.js` | `118e67c295202a5302684f485628c98a3e1f510c` | 33151 |
| `.obsidian/plugins/obsidian-latex/manifest.json` | `e11ad3eb0a17516b643fbd67b3b8abbaeb12ee9c` | 357 |
| `.obsidian/plugins/obsidian-mind-map/main.js` | `6bcab4a79269eac2345ab26e65a06876a481a22b` | 4003625 |
| `.obsidian/plugins/obsidian-mind-map/manifest.json` | `97a9af843553b402c0cb5a317749eafbb30baac2` | 187 |
| `.obsidian/plugins/obsidian-outliner/main.js` | `0ccbd046a6e1085192486497deb93ef1d9818f08` | 289490 |
| `.obsidian/plugins/obsidian-outliner/manifest.json` | `c4bf487d917fb85e784cdb29a99a08b9472b2c2c` | 285 |
| `.obsidian/plugins/obsidian-outliner/styles.css` | `50310ee52b633138831e8abe6fd6ba5d5f8f4516` | 1095 |
| `.obsidian/plugins/obsidian-vault-changelog/data.json` | `5fa6e58c3669df5e4219e7d35c24ae33b3364d58` | 100 |
| `.obsidian/plugins/obsidian-vault-changelog/main.js` | `79dec935ad2825401ef62bfef5e5a0eeaf908448` | 48049 |
| `.obsidian/plugins/obsidian-vault-changelog/manifest.json` | `60aa2daabfe7f1fbd039f4c15fb9ffa40ae1f3e5` | 291 |
| `.obsidian/plugins/recent-files-obsidian/data.json` | `7f9eabf49be67615f7a53a3c25726b1c08d7e24a` | 5770 |
| `.obsidian/plugins/recent-files-obsidian/main.js` | `ece8cdd47f7cdab26b3dd0d4d05e9998ae2ab91d` | 178839 |
| `.obsidian/plugins/recent-files-obsidian/manifest.json` | `f3b68829f426fe0286d0c17c143832819cceed9f` | 264 |
| `.obsidian/plugins/recent-files-obsidian/styles.css` | `5d3f87989429a162d7a4233ecb2df9c78c5fcffe` | 130 |
| `.obsidian/plugins/sliding-panes-obsidian/main.js` | `2b735c43250264d982fa693611adbf6409d4f578` | 104133 |
| `.obsidian/plugins/sliding-panes-obsidian/manifest.json` | `0cebe1278644dae72de9fa5e026cf2f343dd188f` | 339 |
| `.obsidian/plugins/sliding-panes-obsidian/styles.css` | `1bbb3a222f93b00a0ff81b0ab010b2152e55a79d` | 5321 |
| `.obsidian/plugins/smart-random-note/main.js` | `27abde3a0ac38cbf1a3cfe6ab3dbd63e84e0f009` | 173714 |
| `.obsidian/plugins/smart-random-note/manifest.json` | `e94395619d1ebddbde0741dea687d9ea49a24627` | 249 |
| `.obsidian/plugins/table-editor-obsidian/data.json` | `90094659b6f8f38d1d28eb99e2c9e66dfb056778` | 94 |
| `.obsidian/plugins/table-editor-obsidian/main.js` | `ea7effb2f9244481c1c4619cf20377aeb4388f15` | 2745370 |
| `.obsidian/plugins/table-editor-obsidian/manifest.json` | `d174d16522987082407063f2f2c64e7aebb23af2` | 319 |
| `.obsidian/plugins/table-editor-obsidian/styles.css` | `954ea06139a8796e43e6553fd4814c370771a0a8` | 401 |
| `.obsidian/plugins/tag-wrangler/main.js` | `e2cc2fabcc61d4bc4cbe354a58ee260ad02ce829` | 840034 |
| `.obsidian/plugins/tag-wrangler/manifest.json` | `24159ba47149eec556f94ce77ec2e94f30d7cf6e` | 206 |
| `.obsidian/plugins/tag-wrangler/styles.css` | `d58564c8783aef2c8bd1c2f4025c9edf44cc5994` | 4118 |
| `.obsidian/plugins/templater-obsidian/data.json` | `f8cc35cb682552c727a6fed9b3a415c45831fc84` | 510 |
| `.obsidian/plugins/templater-obsidian/main.js` | `220d75f9d066ff7b5e69438356ca4723179ad3e1` | 982318 |
| `.obsidian/plugins/templater-obsidian/manifest.json` | `4ce8d826c29097c03d952a0d950f845eaadc118d` | 271 |
| `.obsidian/plugins/templater-obsidian/styles.css` | `bd49089fde4e3723bfda7ee8d72e98b6db5c8fc8` | 5366 |
| `.obsidian/plugins/wikilinks-to-mdlinks-obsidian/main.js` | `17548c620e8dcddd14d143f4a9d5c1651cdebfdb` | 33464 |
| `.obsidian/plugins/wikilinks-to-mdlinks-obsidian/manifest.json` | `a5a14166bc0ddf93324fb04d57f7f5bee4cfa57f` | 305 |
| `.obsidian/starred.json` | `43950404e7869de602869aba5f8cd35a8ef14380` | 1015 |
| `.obsidian/themes/Clean theme.css` | `dcec21148a7fe50463f4752c2a081c187acab87d` | 7777 |
| `.obsidian/themes/Notation.css` | `923454e1117fe0da20b28dd2654209d4147e5783` | 21699 |
| `.obsidian/themes/Warmth.css` | `8fc2c91623f2b890d17dd1c741a08d9044b4275a` | 9358 |
| `.obsidian/workspace` | `f0cc1bfd788548062ee6b84af4b4bf5ae58dbe09` | 7364 |
| `.obsidian/workspaces.json` | `9e26dfeeb6e641a33dae4961196235bdb965b21b` | 2 |
| `.obsidian/zk-prefixer.json` | `eeefe262d3d1f43a07409ff475644fb100a6c92d` | 83 |

## qual-review-and-solutions — non-content file (no ext) (59 rows)

Direct read: repository identifier only.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `.sparkleshare` | `28260a2a410412c2d0236b8103336c6d269b825e` | 64 |
| `Algebra/Review Doc/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Algebra/Review Doc/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `Algebra/Review Doc/Makefile` | `47bf66a7b4fe28310ce4d14cad61b52e3b4f6a56` | 2658 |
| `Algebra/Review Doc/figures` | `8887e4674fc8c50b4bfa37efe3f10e90ab615841` | 18 |
| `Algebra/Review Doc/sections/Doc/sections/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Algebra/UGA Question (with solutions)/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `Algebra/UGA Question (with solutions)/Makefile` | `d08e56350c904979de43a8fa12021c8d6f23de6c` | 2647 |
| `Algebra/UGA Question (with solutions)/figures` | `15e166947d6a4e41b23496556ac5a33d83fffcb6` | 39 |
| `Algebra/UGA Question (with solutions)/sections` | `d8eafc036ca2c9d0a23d8f90683c4344d5747c7c` | 40 |
| `Algebra/UGA Questions (no solutions)/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Algebra/UGA Questions (no solutions)/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `Algebra/UGA Questions (no solutions)/Makefile` | `669a7ae04b5314b526e649990ad2da365947e05f` | 2647 |
| `Algebra/UGA Questions (no solutions)/sections/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Complex Analysis/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Complex Analysis/Review Doc/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Complex Analysis/Review Doc/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `Complex Analysis/Review Doc/Makefile` | `a36479ea9bf70416427d7a1994fd64548e0a11d9` | 2648 |
| `Complex Analysis/Review Doc/figures` | `8887e4674fc8c50b4bfa37efe3f10e90ab615841` | 18 |
| `Complex Analysis/UGA Question (no solutions)/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Complex Analysis/UGA Question (no solutions)/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `Complex Analysis/UGA Question (no solutions)/Makefile` | `af7086dc11ff6de226387e2615e2fd8b7d7cc260` | 2646 |
| `Complex Analysis/UGA Question (no solutions)/figures` | `8887e4674fc8c50b4bfa37efe3f10e90ab615841` | 18 |
| `Complex Analysis/UGA Question (no solutions)/sections/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Complex Analysis/UGA Question (no solutions)/sections/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Complex Analysis/UGA Question (with solutions)/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `Complex Analysis/UGA Question (with solutions)/Makefile` | `95a5ef9d6d28cc9bd7bccdc750798870cd184c3e` | 2647 |
| `Complex Analysis/UGA Question (with solutions)/figures` | `144220f4aa0ea0e93a2779a19d382565b471f1ec` | 38 |
| `Complex Analysis/UGA Question (with solutions)/sections` | `0eddf7a236a416131a35377b9282b1e19d27caf2` | 39 |
| `Prelims/sections/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Real Analysis/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Real Analysis/Resources/Example Solutions/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Real Analysis/Resources/Folland Questions/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Real Analysis/Review Doc/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `Real Analysis/Review Doc/Makefile` | `61cdc78fa8017c9edbb2f7ec549d09131f73fb57` | 2645 |
| `Real Analysis/Review Doc/figures` | `6b5d059eb83338f4e3479f50f12af8936cd417dd` | 16 |
| `Real Analysis/Review Doc/sections/90_Appendices/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Real Analysis/Review Doc/sections/figures/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Real Analysis/UGA Question (with solutions)/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Real Analysis/UGA Question (with solutions)/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `Real Analysis/UGA Question (with solutions)/Makefile` | `d746d3ef9a333fb6d0474fafcc77145332e9114d` | 2653 |
| `Real Analysis/UGA Question (with solutions)/figures` | `15e166947d6a4e41b23496556ac5a33d83fffcb6` | 39 |
| `Real Analysis/UGA Question (with solutions)/sections` | `d8eafc036ca2c9d0a23d8f90683c4344d5747c7c` | 40 |
| `Real Analysis/UGA Questions (no solutions)/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Real Analysis/UGA Questions (no solutions)/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `Real Analysis/UGA Questions (no solutions)/Makefile` | `130a1c1622c136153529c73c16c09582c86050aa` | 2653 |
| `Real Analysis/UGA Questions (no solutions)/figures` | `6b5d059eb83338f4e3479f50f12af8936cd417dd` | 16 |
| `Topology/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Topology/ReviewDoc/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `Topology/ReviewDoc/Makefile` | `f520f26d061ed0b8a6b65da5a75ff08454f1cb0f` | 2648 |
| `Topology/ReviewDoc/figures` | `6b5d059eb83338f4e3479f50f12af8936cd417dd` | 16 |
| `Topology/Todo/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Topology/UGA_Questions_no_solutions/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `Topology/UGA_Questions_no_solutions/Makefile` | `4e61c17caf3a8e4455a6bceed6ad8ec24b574be3` | 2648 |
| `Topology/UGA_Questions_no_solutions/figures` | `0ed601d4bdc1380a8b5234828ba184e4d8a9be11` | 48 |
| `Topology/UGA_Questions_no_solutions/sections` | `d7ea592540e56fdba3d442631d3467402a538a06` | 40 |
| `Topology/UGA_Questions_with_solutions/.pandoc` | `e14f1f82f21cf9065d4670661adecd5f16987add` | 27 |
| `Topology/UGA_Questions_with_solutions/Makefile` | `4517b06afe35097e6ae140369a8e5d1dfaa90558` | 2648 |
| `Topology/UGA_Questions_with_solutions/figures` | `6b5d059eb83338f4e3479f50f12af8936cd417dd` | 16 |

## qual-review-and-solutions — non-content file (.bib) (5 rows)

Direct read: zero-byte BibTeX file; no bibliographic entries.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `Algebra/UGA Question (with solutions)/UGA_Algebra_Qual_Solutions.bib` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | 0 |
| `Algebra/UGA Questions (no solutions)/UGA_Algebra_Qual_Questions.bib` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | 0 |
| `Complex Analysis/Review Doc/Complex_Analysis_Qual_Notes.bib` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | 0 |
| `Real Analysis/Review Doc/Real_Analysis_Qual_Notes.bib` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | 0 |
| `Topology/UGA_Questions_with_solutions/UGA_Topology_Qual_Solutions.bib` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | 0 |

## qual-review-and-solutions — empty file (0 bytes) (1 rows)

Direct read: zero-byte file.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `Complex Analysis/UGA Question (no solutions)/sections/003_Morera.md` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | 0 |

## qual-review-and-solutions — non-content file (.json) (1 rows)

Direct read: editor settings only; no project data.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `Real Analysis/Review Doc/.vscode/settings.json` | `73324e5583ecab52cf908417f77327533309e6d5` | 75 |

## make-me-a-qual — editor config (1 rows)

Direct read: editor, plugin, theme, workspace, or ignore configuration; no authored mathematical, bibliographic, provenance, or figure payload.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `.gitignore` | `cb770ba38959f2e9e30adb008b61854f95f26b75` | 45 |

## make-me-a-qual — non-content file (no ext) (17 rows)

Direct read: repository identifier only.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `.sparkleshare` | `d86381affee18217d02cab252bf73f9323ab1d9d` | 64 |
| `Makefile` | `a3ff4026f54fccc50124bd2d6942b778d51c1649` | 1230 |
| `Questions/Algebra/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Questions/Algebra/Extra/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Questions/Algebra/Harvard/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Questions/Complex_Analysis/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Questions/Complex_Analysis/Emory/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Questions/Complex_Analysis/Harvard/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Questions/Complex_Analysis/UGA/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Questions/Real_Analysis/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Questions/Real_Analysis/Emory/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Questions/Real_Analysis/Extra/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Questions/Real_Analysis/UGA/Fall 2019/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Questions/Real_Analysis/UGA/Makefile` | `2592e06087af33c9752861adab3a4aee2b2f8876` | 545 |
| `Questions/Topology/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Questions/Topology/UCSD/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Questions/Topology/UGA/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |

## make-me-a-qual — web tool / notebook checkpoint (WS7) (28 rows)

Direct read: literal folder marker.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `Webtool/.empty` | `da1585c347ba6fbe32f75d9ebe5c4531dfe88e5f` | 13 |
| `Webtool/Frontend/Complex_Analysis.json` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | 0 |
| `Webtool/Frontend/Real_Analysis.json` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | 0 |
| `Webtool/Frontend/css/bootstrap-grid.css` | `916ec629cadd52186644081db4fe6c408321e371` | 25510 |
| `Webtool/Frontend/css/bootstrap-grid.css.map` | `058beb4546d9e898e51c4c95066feccc69bdfa65` | 31527 |
| `Webtool/Frontend/css/bootstrap-grid.min.css` | `edb16cb64452334515955e36a29cc31c6bba8549` | 18528 |
| `Webtool/Frontend/css/bootstrap-grid.min.css.map` | `edae8e65814f4c9bfa16a9a17c5ea8d2649d227a` | 12300 |
| `Webtool/Frontend/css/bootstrap-reboot.css` | `f5d4414c1d2377543f610917e084a7e1c9998cb1` | 5916 |
| `Webtool/Frontend/css/bootstrap-reboot.css.map` | `67c00c3351a4bf7070bc244ba8cdae942b862b2d` | 9322 |
| `Webtool/Frontend/css/bootstrap-reboot.min.css` | `7bf239551733124399d3c21edcba185e84e660ab` | 4707 |
| `Webtool/Frontend/css/bootstrap-reboot.min.css.map` | `fa2cf1266b8821c836593e7a6e8fd40bcf652940` | 2668 |
| `Webtool/Frontend/css/bootstrap.css` | `1038ebcb333a0eeef13999ee12988cf17a9c474c` | 191738 |
| `Webtool/Frontend/css/bootstrap.css.map` | `09b7cf110637d156d9ff80bfc3b306a1526d73eb` | 235595 |
| `Webtool/Frontend/css/bootstrap.min.css` | `a8da0748bcc84979744aab276e6804ed48e7220b` | 150996 |
| `Webtool/Frontend/css/bootstrap.min.css.map` | `74462f2c33b69f3db31b0f4ab7c99997666173f7` | 68044 |
| `Webtool/Frontend/css/style.css` | `360c4f6aabe43f96719b1c3ae855a78d56572aaf` | 33 |
| `Webtool/Frontend/fonts/glyphicons-halflings-regular.eot` | `b93a4953fff68df523aa7656497ee339d6026d64` | 20127 |
| `Webtool/Frontend/fonts/glyphicons-halflings-regular.svg` | `94fb5490a2ed10b2c69a4a567a4fd2e4f706d841` | 108738 |
| `Webtool/Frontend/fonts/glyphicons-halflings-regular.ttf` | `1413fc609ab6f21774de0cb7e01360095584f65b` | 45404 |
| `Webtool/Frontend/fonts/glyphicons-halflings-regular.woff` | `9e612858f802245ddcbf59788a0db942224bab35` | 23424 |
| `Webtool/Frontend/fonts/glyphicons-halflings-regular.woff2` | `64539b54c3751a6d9adb44c8e3a45ba5a73b77f0` | 18028 |
| `Webtool/Frontend/js/bootstrap.min.js` | `d9c72dfc1a2228e2bf64652d839a75e5e50968da` | 46653 |
| `Webtool/Frontend/js/jquery.min.js` | `4d9b3a258759c53e7bc66b6fc554c51e2434437c` | 86927 |
| `Webtool/Frontend/js/popper.min.js` | `8bf4ff8f3c00444822ac0b6ac574bae9a785cf66` | 20560 |
| `Webtool/Frontend/js/scripts.js` | `96e3276525d431cc8dfacdbe556b182b51728b70` | 5526 |
| `Webtool/__pycache__/app.cpython-38.pyc` | `13b40c608197cd552bea5ceb9aadbaeaaa693226` | 2445 |
| `Webtool/app.py` | `54158c9590e05ddc6b9caa163e68cad33d0aacd9` | 2834 |
| `Webtool/dollar_math.lua` | `b844a497aa6775830df71274d9cf9b5d3e3cb8fc` | 1078 |

## make-me-a-qual — non-content file (.py) (1 rows)

Direct read: build helper only; it reads migrated YAML and emits a derived document.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `make_md_doc.py` | `6e9855f7ba9322dd54730fff0c2e47202de190ab` | 1239 |

## make-me-a-qual — non-content file (.sh) (2 rows)

Direct read: build or text-normalization shell script only; no authored corpus payload.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `replace.sh` | `d30310ff5c33485c8eafff6704d1001338b18a7c` | 431 |
| `unicode_replace.sh` | `f6d8379f361288baca6932b6bca73bb611dac000` | 162 |

## math-flashcards — repo documentation / build tooling (.agents/apkg_diff.py) (1 rows)

Direct read: APKG comparison tool only; no deck payload.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `.agents/apkg_diff.py` | `cef78bd111672ea63ad3ff72e2a37700e088ec5b` | 4676 |

## math-flashcards — repo documentation / build tooling (.agents/apkg_to_decks.py) (1 rows)

Direct read: APKG-to-deck conversion tool only; no deck payload.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `.agents/apkg_to_decks.py` | `bb8164063750072b28f6ee1d2ee554197fa27682` | 7138 |

## math-flashcards — repo documentation / build tooling (.agents/check-decks.py) (1 rows)

Direct read: deck-shape checker only; no deck payload.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `.agents/check-decks.py` | `f9ba819fde0f697b3718a31f9f96c5fee5e31b97` | 1488 |

## math-flashcards — editor config (1 rows)

Direct read: editor, plugin, theme, workspace, or ignore configuration; no authored mathematical, bibliographic, provenance, or figure payload.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `.gitignore` | `7a60b85e148f80966a550e5ab6a762a907c69ca6` | 19 |

## math-flashcards — repo documentation / build tooling (justfile) (1 rows)

Direct read: build recipe only; no deck payload.

| Source path | Git object | Bytes |
| --- | --- | --- |
| `justfile` | `01dcfbc23367df03dd4bc89e0dcbab4789a3145d` | 479 |

## Disposition

Every reviewed row contains no authored mathematical, bibliographic, provenance, or figure content.
The rows remain `dropped` as operational, generated, empty, or editor artifacts.
Content-bearing source rows are not included in this review; they remain governed by their source-review records and direct target comparisons.

The five empty BibTeX rows were read as zero-byte blobs.
The web-tool JSON rows were also read as zero-byte blobs.
The four Git path-pointer rows in `qual-wiki` and the corresponding path-pointer rows in `qual-review-and-solutions` were read as pointers, not file content; their target directories are separately present in the source inventory.
