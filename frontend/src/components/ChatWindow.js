import { Header } from "./Header";
import { InputBox } from "./InputBox";
import { MessageBubble } from "./MessageBubble";
import { sendMessageToBackend } from "../services/chatService.js";

export function ChatWindow() {
  const container = document.createElement("div");
  container.className = "chat-container";

  const header = Header();
  const chatBox = document.createElement("div");
  chatBox.className = "chat-box";
  chatBox.id = "chat-box";

  const inputArea = document.createElement("div");
  inputArea.className = "input-area";

  const inputBox = InputBox(async (message) => {
    // When chat starts for the first time
    if (!container.classList.contains("chat-started")) {
      container.classList.add("chat-started");
      header.style.display = "none";
    }

    // Append user's message
    const userMsg = MessageBubble(message, "user");
    chatBox.appendChild(userMsg);
    chatBox.scrollTop = chatBox.scrollHeight;
        
    try {
      // Send message to backend and get response
      const aiReply = await sendMessageToBackend(message);

      // Append AI response message
      const aiMsg = MessageBubble(aiReply, "ai");
      chatBox.appendChild(aiMsg);
      chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
      // Handle network/backend errors gracefully
      const errorMsg = MessageBubble(
        "⚠️ Unable to reach AI service. Please try again later.",
        "ai"
      );
      chatBox.appendChild(errorMsg);
      console.error("Chat error:", error);
    }
  });

  inputArea.appendChild(inputBox);

  container.appendChild(header);
  container.appendChild(chatBox);
  container.appendChild(inputArea);

  return container;
}
