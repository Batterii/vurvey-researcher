//import { Client } from '../Client';

//export class CoderAgent {
//  private client: Client;

//  constructor() {
//    this.client = new Client();
//  }

//  async generateCode(researchState: any) {
//    const prompt = [{
//      role: "system",
//      content: "You are a skilled programmer tasked with generating code based on research findings."
//    }, {
//      role: "user",
//      content: `Generate code based on the following research: ${JSON.stringify(researchState)}`
//    }];

//    const response = await this.client.chat.completions.create({
//      model: "gpt-4",
//      messages: prompt,
//    });

//    return response.choices[0].message.content;
//  }
//}
