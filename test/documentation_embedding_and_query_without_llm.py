#!/usr/bin/env python

# Load the retriever
def load_retriever(embeddings, docstore_collection_name):
     # Set up parent and child text splitters
     parent_splitter = RecursiveCharacterTextSplitter(chunk_size=2000)
     child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)
     docstore = MongoDBStore(
         connection_string=MONGODB_CONNECTION_STRING,
         db_name=MONGODB_DATABASE_NAME,
         collection_name=docstore_collection_name,
     )
     vectorstore = PGVector(
         collection_name="ai_embeddings",
         connection_string=POSTGRESQL_CONNECTION_STRING,
         embedding_function=embeddings,
         use_jsonb=True,
     )
     retriever = ParentDocumentRetriever(
         vectorstore=vectorstore,
         docstore=docstore,
         child_splitter=child_splitter,
         parent_splitter=parent_splitter,
     )
     return retriever


# Load target docs
def load_docs_target(target_docs_path):
     loader = DirectoryLoader(
         target_docs_path.resolve(),
         glob="**/*.md",
         loader_cls=UnstructuredMarkdownLoader,
     )
     docs = loader.load()
     return docs

retriever = load_retriever(embeddings, args.collection)

# TODO If no docs from search then add, only uncomment next line on fresh db
docs = load_docs_target(args.docs)
print("Number of target docs:", len(docs))
retriever.add_documents(docs)

query = "1CI/CD is about"

docs = retriever.get_relevant_documents(query)

