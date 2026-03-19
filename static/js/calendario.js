/* ─── Constantes ─── */
    const DAYS   = ['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sábado'];
    const MONTHS = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];
    const SLOTS  = [
      '09:00','09:30','10:00','10:30','11:00','11:30',
      '12:00','12:30','13:00','14:00','14:30','15:00',
      '15:30','16:00','16:30','17:00','17:30','18:00'
    ];

    /* Genera clave de fecha con offset de días */
    const dk = n => { const d = new Date(); d.setDate(d.getDate() + n); return d.toISOString().slice(0, 10); };

    /* Slots ya ocupados por día (reemplazar con API real) */
    const TAKEN = {
      [dk(0)]: ['09:00','10:00','14:00','15:30'],
      [dk(1)]: ['11:00','12:00','16:00'],
      [dk(2)]: ['09:30','13:00','17:00','18:00'],
    };

    const now    = new Date();
    const todayK = dk(0);
    const nowM   = now.getHours() * 60 + now.getMinutes();

    /* ─── Estado ─── */
    let sel = { day: null, slot: null };

    /* ─── Helpers Bootstrap Tab ─── */
    const goTab = id => bootstrap.Tab.getOrCreateInstance(document.getElementById(id)).show();

    /* Actualiza círculos del indicador de pasos */
    function markSteps(active) {
      [1, 2, 3].forEach(n => {
        const lnk = document.getElementById(`tab${n}`);
        const cir = document.getElementById(`c${n}`);
        lnk.classList.remove('active', 'done');
        if      (n === active) { lnk.classList.add('active'); cir.textContent = n; }
        else if (n <  active)  { lnk.classList.add('done');   cir.textContent = '✓'; }
        else                   { cir.textContent = n; }
      });
    }

    /* ─── Paso 1: construir calendario ─── */
    for (let i = 0; i < 3; i++) {
      const d = new Date(); d.setDate(d.getDate() + i);
      const key = d.toISOString().slice(0, 10);
      const sun = d.getDay() === 0;

      const card = Object.assign(document.createElement('div'), {
        className: 'day-card' + (sun ? ' disabled' : '')
      });
      card.innerHTML = `
        <div class="day-name">${DAYS[d.getDay()]}</div>
        <div class="day-num">${String(d.getDate()).padStart(2, '0')}</div>
        <div class="day-month">${MONTHS[d.getMonth()]}</div>
        ${sun ? '<small style="font-size:.56rem;color:#444">CERRADO</small>' : ''}
      `;
      card.dataset.label = `${DAYS[d.getDay()]} ${d.getDate()} de ${MONTHS[d.getMonth()]}`;
      if (!sun) card.onclick = () => pickDay(card, key, card.dataset.label);
      document.getElementById('dayGrid').appendChild(card);
    }

    function pickDay(el, key, label) {
      document.querySelectorAll('.day-card').forEach(c => c.classList.remove('active'));
      el.classList.add('active');
      sel = { day: { key, label }, slot: null };
      document.getElementById('btnTo2').disabled = true;

      const taken = TAKEN[key] || [];
      const box   = document.getElementById('slotsBox');
      const grid  = Object.assign(document.createElement('div'), { className: 'slots-grid' });
      let avail   = 0;

      SLOTS.forEach(t => {
        const [h, m] = t.split(':').map(Number), sm = h * 60 + m;
        const off    = (key === todayK && sm <= nowM + 30) || taken.includes(t);
        if (!off) avail++;
        const s = Object.assign(document.createElement('div'), {
          className: 'slot' + (off ? ' taken' : '')
        });
        s.innerHTML = `${t}<span class="slot-dot"></span>`;
        if (!off) s.onclick = () => pickSlot(s, t);
        grid.appendChild(s);
      });

      box.innerHTML = '';
      if (avail) box.appendChild(grid);
      else box.innerHTML = '<div class="no-slots">Sin horarios disponibles 😔</div>';
    }

    function pickSlot(el, t) {
      document.querySelectorAll('.slot').forEach(s => s.classList.remove('active'));
      el.classList.add('active');
      sel.slot = t;
      document.getElementById('btnTo2').disabled = false;
    }

    /* ─── Navegación ─── */
    document.getElementById('btnTo2').onclick = () => { goTab('tab2'); markSteps(2); };
    document.getElementById('bk1').onclick    = () => { goTab('tab1'); markSteps(1); };

    document.getElementById('btnTo3').onclick = () => {
      // Llenar resumen con los datos del formulario
      document.getElementById('rDia').textContent    = sel.day.label;
      document.getElementById('rHora').textContent   = sel.slot;
      document.getElementById('rNombre').textContent = `${document.getElementById('fN').value.trim()} ${document.getElementById('fA').value.trim()}`;
      document.getElementById('rEmail').textContent  = document.getElementById('fE').value.trim();
      document.getElementById('rTel').textContent    = document.getElementById('fT').value.trim();
      document.getElementById('rPago').textContent   = document.querySelector('input[name="pago"]:checked').value;
      goTab('tab3'); markSteps(3);
    };

    document.getElementById('bk2').onclick = () => { goTab('tab2'); markSteps(2); };

    /* ─── Validación en vivo (Paso 2) ─── */
    ['fN', 'fA', 'fE', 'fT'].forEach(id =>
      document.getElementById(id).addEventListener('input', () => {
        const ok = document.getElementById('fN').value.trim()
                && document.getElementById('fA').value.trim()
                && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(document.getElementById('fE').value)
                && document.getElementById('fT').value.trim().length >= 7;
        document.getElementById('btnTo3').disabled = !ok;
      })
    );

    /* ─── Confirmar cita ─── */
    document.getElementById('btnOk').onclick = () => {
      const t = document.getElementById('toast');
      t.textContent = `✅ ¡Cita reservada! ${sel.day.label} · ${sel.slot}`;
      t.classList.add('show');
      setTimeout(() => { t.classList.remove('show'); location.reload(); }, 3500);
    };