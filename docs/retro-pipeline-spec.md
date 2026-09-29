# ТЗ: конвейер «campaign raw → results.csv → verdict pack» (автоматизация ретро-анализа)

**Статус:** ratified (W1 draft, W2 review + filing). Источник драфта — W1; две строки с тегом `[W2 filing addition]` добавлены при файлинге, остальное дословно.

## 1. Цель

Убрать руки с детерминированных шагов между сырыми артефактами кампании и готовым verdict pack. Один запуск на входе, воспроизводимый пак на выходе.

## 2. Граница (binding)

Машина — сборка, человек — суждение:

- **ALLOWLIST (механика, делает машина):** exit_code→suite_result; timestamp→run_ref; сборка строк из распарсенных полей без интерпретации; подсчет mutation_score (= caught/seeded, SCORER_VERSION + раздел scorer) и native_rate (доля срабатываний нативного поля verdict-модели; instrument reading, uncalibrated, transparency only, never gates) [W2 rename ad9f475-acceptance: было Reg/Reg*; ASCII-safe]; знаменатель mutation_score — ТОЛЬКО seeded-break subset (baseline/fix controls excluded; W1 operationalizes which conditions count — recommended break+drift=60 on H4 design); числитель-эквивалентность (absent ⟺ caught) UNTESTED — ноль ненулевых кейсов (H4: 0/120 = 0/60 = 0 в любой рамке, число не меняется, дефиниция обязана); первый ненулевой кейс переоткрывает тождество; проверка пустоты drift-diff (boolean, без чтения содержимого); прогон verdictgate; предзаполнение скелета sign-off таблицы; вшивание SHA входов в пак. Нормализация байт-сохраняющая по дефолту [W2 filing addition: никакого case/whitespace-фолдинга без явного перечисления; перечисленного нет — значит побайтово].
- **Всё остальное — человек по дефолту:** маппинг behavior/tier, замены, нарратив, уроки, сама подпись, **любая новая деривация, которой нет в allowlist**. Новый столбец в results.csv без рулинга = стоп конвейера, не импровизация.

## 3. Интерфейсы

- Вход: campaign raw обязан содержать run-логи (JSONL), пины версий/SHA, таймстампы, exit-коды, сырые вердикты прогонов. Нет обязательного поля — fail fast с именем поля, не додумывание.
- Середина: frozen-схема results.csv (ссылка, не копия).
- Выход: verdict pack фиксированного layout (verdict JSON + MD + скелет sign-off + штамп-блок + SHA входов).

## 4. Стадии

parse → normalize → verdict (verdictgate) → assemble → pin. Каждая стадия детерминирована и идемпотентна: повтор на тех же входах = побайтово тот же выход.

## 5. Приемка

Перезапуск на артефактах OpenClaw batch #1 воспроизводит опубликованный вердикт побайтово (golden-тест, та же планка что у goldens скорера).

## 6. Не-цели

live-анализ во время ранов; замена суждения асессора; автоподпись (таблица предзаполнена — подписывает человек).
