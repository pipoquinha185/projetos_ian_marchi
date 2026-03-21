import { useState } from 'react'
import './App.css' // <-- Aqui você conecta o design ao seu HTML

function App() {
  // Seus estados (a "memória" do formulário)
  const [nome, setNome] = useState('')
  const [cpf, setCpf] = useState('')
  const [ano, setAno] = useState('')
  const [curso, setCurso] = useState('Engenharia da computação')
  const [mensagem, setMensagem] = useState('')

  // Função para enviar os dados para o Flask
  const enviarDados = async () => {
    // Aqui faremos a conexão com o Python depois
    console.log("Botão clicado!", { nome, cpf, ano, curso })
    setMensagem(`Processando matrícula para ${nome}...`)
    try {
    // Note o http:// e apenas UM await
    const resposta = await fetch("http://127.0.0.1:5000/matricular", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        nome: nome,
        cpf: cpf,
        ano: ano,
        curso: curso
      }),
    });

    const dados = await resposta.json();

    if (dados.sucesso) {
      setMensagem(`Matrícula gerada: ${dados.matricula}`);
    } else {
      setMensagem(`Erro: ${dados.mensagem || dados.erro}`);
    }
  } catch (error) {
    setMensagem("Erro: Não foi possível conectar ao servidor.");
  }
    
  }

  return (
    <div className="container">
      <h1>Matrícula Online</h1>

      <div className="formulario">
        <label>Nome Completo:</label>
        <input 
          type="text" 
          value={nome} 
          onChange={(e) => setNome(e.target.value)} 
          placeholder="Ex: Joao Evandro"
        />

        <label>CPF (apenas números):</label>
        <input 
          type="text" 
          value={cpf} 
          onChange={(e) => setCpf(e.target.value)} 
          placeholder="000.000.000-00"
        />

        <label>Ano de Nascimento:</label>
        <input 
          type="number" 
          value={ano} 
          onChange={(e) => setAno(e.target.value)} 
        />

        <label>Curso:</label>
        <select value={curso} onChange={(e) => setCurso(e.target.value)}>
          <option value="Engenharia da computação">Engenharia da computação</option>
          <option value="Psicologia">Psicologia</option>
          <option value="Medicina">Medicina</option>
          <option value="Odontologia">Odontologia</option>
        </select>

        <button onClick={enviarDados}>Gerar Matrícula</button>
      </div>

      {/* Só mostra a caixa de mensagem se houver algo escrito nela */}
      {mensagem && <div className="resultado">{mensagem}</div>}
    </div>
  )
}

export default App