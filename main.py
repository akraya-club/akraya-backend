import argparse
from ctransformers import AutoModelForCausalLM

parser = argparse.ArgumentParser(description='Generate text using AKRAYAv1 model.')
parser.add_argument('--question', type=str, help='User question in quotes')
parser.add_argument('--temperature', type=float, help='Temperature for text generation', default=0.3)
parser.add_argument('--max_new_tokens', type=int, help='Maximum number of new tokens', default=1024)
parser.add_argument('--top_k', type=int, help='Top-k value for sampling', default=40)
parser.add_argument('--top_p', type=float, help='Top-p value for sampling', default=0.95)
parser.add_argument('--repetition_penalty', type=float, help='Repetition penalty for sampling', default=1.1)
parser.add_argument('--last_n_tokens', type=int, help='Number of last tokens for repetition penalty', default=64)
parser.add_argument('--seed', type=int, help='Seed value for sampling tokens', default=-1)
parser.add_argument('--batch_size', type=int, help='Batch size for evaluating tokens in a single prompt', default=512)
parser.add_argument('--threads', type=int, help='Number of threads for evaluating tokens', default=16)
parser.add_argument('--stream', action='store_true', help='Whether to stream the generated text', default=True)
parser.add_argument('--reset', action='store_true', help='Whether to reset the model state before generating text', default=False)
args = parser.parse_args()

print("Used parameters:")
for arg in vars(args):
    print(f"  --{arg}: {getattr(args, arg)}")

if args.question is None:
    args.question = input("Enter the user's question: ")

print("\nModel: Booting")

llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-13B-Chat-GGML") # TheBloke/Llama-2-7B-Chat-GGML IS FASTER
print("Model: Booted")

print("Model: Starting")

main_prompt = """You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.The user's question is enclosed in brackets: [{}]""".format(args.question)
# Example of streaming output
for text in llm(main_prompt,
               max_new_tokens=args.max_new_tokens,
               top_k=args.top_k,
               top_p=args.top_p,
               temperature=args.temperature,
               repetition_penalty=args.repetition_penalty,
               last_n_tokens=args.last_n_tokens,
               seed=args.seed,
               batch_size=args.batch_size,
               threads=args.threads,
               stop=None,
               stream=args.stream,
               reset=args.reset):
    print(text, end="", flush=True)



# Example Promt: I talk to my girlfriend about things that bother me. For instance, if she does something I think is wrong, like snitching people for no reason, I let her know it upsets me. I tell her that if these issues, especially those involving my ex, continue and she doesn't try to fix them, I might end our relationship.
