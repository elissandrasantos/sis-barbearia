from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Armazena os agendamentos
appointments = []

# Definir horários disponíveis
available_times = ['08:00', '09:00', '10:00', '11:00', '12:00',
                   '14:00', '15:00', '16:00', '17:00', '18:00']

# Preços dos serviços
service_prices = {
    'cabelo': 15.00,
    'barba': 10.00,
    'sobrancelha': 5.00
}

@app.route('/', methods=['GET', 'POST'])
def agendamento():
    if request.method == 'POST':
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        servicos = request.form.getlist('servicos')
        horario = request.form.get('horario')

        # Verificar se o horário está disponível
        occupied_times = [appointment['horario'] for appointment in appointments]
        if horario in occupied_times:
            error_message = 'Horário indisponível. Por favor, escolha outro horário.'
            # Atualizar horários disponíveis
            available = [time for time in available_times if time not in occupied_times]
            return render_template('index.html', available_times=available, service_prices=service_prices, error_message=error_message)
        
        # Calcular o preço total
        total_price = sum([service_prices[servico] for servico in servicos])

        # Armazenar o agendamento
        appointment = {
            'nome': nome,
            'telefone': telefone,
            'servicos': servicos,
            'horario': horario,
            'total_price': total_price
        }
        appointments.append(appointment)

        # Renderizar a página de confirmação
        return render_template('confirmacao.html', nome=nome, telefone=telefone, servicos=servicos, horario=horario, total_price=total_price, service_prices=service_prices)
    else:
        # Atualizar horários disponíveis
        occupied_times = [appointment['horario'] for appointment in appointments]
        available = [time for time in available_times if time not in occupied_times]
        return render_template('index.html', available_times=available, service_prices=service_prices)

@app.route('/agenda')
def agenda():
    return render_template('agenda.html', appointments=appointments, service_prices=service_prices)

if __name__ == '__main__':
    app.run(debug=True)
